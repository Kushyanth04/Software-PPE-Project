from pathlib import Path
import json
import logging
from datetime import datetime
from anthropic import Anthropic
from dataclasses import dataclass, asdict
from typing import Dict, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class TestGenerationResult:
    """Results from LLM test generation"""
    problem_id: str
    title: str
    difficulty: str
    prompt_type: str
    test_content: str
    generation_timestamp: str
    model_used: str
    total_test_cases: int = 0
    metadata: Dict = None

class LLMTestGenerator:
    def __init__(self, dataset_path: Path):
        """Initialize the test generator"""
        self.dataset_path = Path(dataset_path)
        if not self.dataset_path.exists():
            raise FileNotFoundError(f"Dataset path does not exist: {dataset_path}")
        
        # Create base output directory with timestamp matching dataset convention
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.base_output_path = Path("dataset_leetcode") / f"llm_generated_tests_{timestamp}"
        self.base_output_path.mkdir(parents=True, exist_ok=True)
        
        # Set up logging in the base directory
        self._setup_logging()
        
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        self.anthropic = Anthropic(api_key=api_key)

    def _setup_logging(self):
        """Setup logging configuration"""
        log_path = self.base_output_path / 'logs'
        log_path.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path / f'generation_{timestamp}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _create_zero_shot_prompt(self, problem_content: str, template_content: str) -> str:
        """Zero-shot prompt that doesn't see any existing tests"""
        return f"""Generate pytest test cases for this Python LeetCode problem.

Problem Description:
{problem_content}

Python Template:
{template_content}

Requirements:
1. Use pytest's parametrize decorator for multiple test cases
2. Include both basic test cases from the problem description and edge cases
3. Add proper type hints for parameters
4. Include a TestSolution class with a test method
5. Use assert statements to verify the solution
6. Follow the exact import format from the template file
7. Match the test method name with the method in the template

Generate only the test code without any explanations."""

    def _create_few_shot_prompt(self, problem_content: str, template_content: str, example_test: str, test_cases_data: dict) -> str:
        """Few-shot prompt that learns from both test file and test cases"""
        return f"""Generate pytest test cases for this Python LeetCode problem.

Problem Description:
{problem_content}

Python Template:
{template_content}

Example Test File Format:
{example_test}

Example Test Cases and Expected Outputs:
{json.dumps(test_cases_data, indent=2)}

Requirements:
1. Follow the exact same format as the example test file
2. Use the test cases structure shown in the example
3. Generate additional test cases beyond the examples
4. Include edge cases and corner cases
5. Maintain the same pytest parametrize format
6. Keep the same import style and class structure

Generate only the test code without any explanations."""

    def _get_problem_base_name(self, difficulty: str, problem_id: str, title: str) -> str:
        """Generate consistent base name for problem files"""
        return f"{difficulty.lower()}_{problem_id}_{title.lower().replace(' ', '_')}"

    def _save_generated_test(self, problem_dir: Path, result: TestGenerationResult):
        """Save generated test following dataset naming convention"""
        base_name = self._get_problem_base_name(
            result.difficulty,
            result.problem_id,
            result.title
        )
        
        # Create directory structure
        output_dir = self.base_output_path / base_name / result.prompt_type
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Clean up test content
        test_content = result.test_content
        if test_content.startswith('```python'):
            test_content = test_content[9:]
        if test_content.endswith('```'):
            test_content = test_content[:-3]
        test_content = test_content.strip()
        
        # Save files following naming convention
        test_file = output_dir / f"{base_name}_{result.prompt_type}_test.py"
        test_cases_file = output_dir / f"{base_name}_{result.prompt_type}_test_cases.json"
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
            
        with open(test_cases_file, 'w', encoding='utf-8') as f:
            json.dump({
                'problem_id': result.problem_id,
                'title': result.title,
                'difficulty': result.difficulty,
                'prompt_type': result.prompt_type,
                'generation_timestamp': result.generation_timestamp,
                'model_used': result.model_used,
                'test_content': test_content,
                'metadata': result.metadata
            }, f, indent=2)
            
        self.logger.info(f"Saved {result.prompt_type} test to {output_dir}")

    def generate_test_cases(self, problem_dir: Path, prompt_type: str = 'zero-shot') -> TestGenerationResult:
        """Generate test cases using specified prompting strategy"""
        self.logger.info(f"Generating test cases for problem in {problem_dir} using {prompt_type} prompting")
        
        try:
            # Get base name from directory name
            dir_name = problem_dir.name
            
            # Read problem files using the naming convention
            with open(problem_dir / f"{dir_name}_problem.md", 'r', encoding='utf-8') as f:
                problem_content = f.read()
            
            with open(problem_dir / f"{dir_name}_template.py", 'r', encoding='utf-8') as f:
                template_content = f.read()
                
            with open(problem_dir / f"{dir_name}_metadata.json", 'r', encoding='utf-8') as f:
                metadata = json.load(f)

            # Choose prompt strategy
            if prompt_type == 'few-shot':
                # Read both test file and test cases for few-shot
                with open(problem_dir / f"{dir_name}_test.py", 'r', encoding='utf-8') as f:
                    example_test = f.read()
                with open(problem_dir / f"{dir_name}_test_cases.json", 'r', encoding='utf-8') as f:
                    test_cases_data = json.load(f)
                prompt = self._create_few_shot_prompt(problem_content, template_content, 
                                                    example_test, test_cases_data)
            else:
                # Zero-shot only gets problem and template
                prompt = self._create_zero_shot_prompt(problem_content, template_content)
            
            self.logger.info(f"Using {prompt_type} prompting strategy")
            response = self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1500,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            test_content = response.content[0].text
            
            # Create result and save
            result = TestGenerationResult(
                problem_id=metadata['problem_id'],
                title=metadata['title'],
                difficulty=metadata['difficulty'],
                prompt_type=prompt_type,
                test_content=test_content,
                generation_timestamp=datetime.now().isoformat(),
                model_used=response.model,
                metadata=metadata
            )
            
            self._save_generated_test(problem_dir, result)
            return result
            
        except Exception as e:
            self.logger.error(f"Error generating test cases for {problem_dir.name}: {str(e)}")
            raise

def main():
    try:
        if not os.getenv('ANTHROPIC_API_KEY'):
            print("Error: ANTHROPIC_API_KEY not found in environment variables")
            print("Please set your API key in a .env file")
            return
            
        # Use current dataset path
        dataset_path = Path("dataset_leetcode/dataset_20241126_193530")
        print(f"Using dataset directory: {dataset_path}")
        
        generator = LLMTestGenerator(dataset_path)
        
        # Load baseline report to get problem list
        with open(dataset_path / "baseline_report.json", 'r') as f:
            report = json.load(f)
        
        # Generate tests for each problem
        for problem in report['problems']:
            print(f"\nProcessing {problem['title']}...")
            
            # Construct problem directory path
            problem_dir_name = f"{problem['difficulty'].lower()}_{problem['problem_id']}_{problem['title'].lower().replace(' ', '_')}"
            problem_dir = dataset_path / problem_dir_name
            
            print(f"1. Generating zero-shot tests...")
            # Zero-shot only gets problem description and template
            generator.generate_test_cases(problem_dir, 'zero-shot')
            
            print(f"2. Generating few-shot tests...")
            # Few-shot gets problem, template, example tests, and test cases
            generator.generate_test_cases(problem_dir, 'few-shot')
            
            print(f"Completed test generation for {problem['title']}")
        
        print(f"\nGeneration complete! Tests saved in: {generator.base_output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()