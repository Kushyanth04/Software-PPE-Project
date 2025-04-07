from pathlib import Path
import json
import logging
from datetime import datetime
from typing import Dict, Optional, List, Tuple
import os
from anthropic import Anthropic
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

class TestTemplate:
    """Manages test templates for different problem categories"""
    def __init__(self, templates_dir: Path):
        self.templates_dir = templates_dir / "generated_templates"
        if not self.templates_dir.exists():
            raise FileNotFoundError(f"Templates directory not found: {self.templates_dir}")
        self.used_templates = {}
        self._load_templates()

    def _load_templates(self):
        """Load all template files and their metadata"""
        self.templates = {}
        for category_dir in self.templates_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name  # e.g., "easy_array"
                self.templates[category] = []
                
                # Load all template files in the category
                template_files = list(category_dir.glob("*_template_test.py"))
                for template_file in template_files:
                    metadata_file = template_file.parent / f"{template_file.stem.replace('_template_test', '_metadata.json')}"
                    
                    if not metadata_file.exists():
                        continue
                        
                    with open(template_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                        
                    self.templates[category].append({
                        'content': content,
                        'metadata': metadata,
                        'template_id': metadata['template_id'],
                        'target_id': metadata['target_id']
                    })

    def get_template(self, problem: Dict) -> Tuple[str, Dict]:
        """Get appropriate template for a problem based on characteristics"""
        difficulty = problem['difficulty'].lower()
        prob_type = problem['problem_type'].lower()
        category = f"{difficulty}_{prob_type}"
        problem_id = problem['problem_id']
        
        if category not in self.templates:
            raise ValueError(f"No templates found for category: {category}")
        
        # Filter valid templates
        valid_templates = [
            t for t in self.templates[category]
            if (problem_id not in self.used_templates.get(t['template_id'], set()) and
                t['target_id'] != problem_id)
        ]
        
        if not valid_templates:
            raise ValueError(f"No unused templates available for {category}")
        
        # Sort templates by relevance
        sorted_templates = sorted(
            valid_templates,
            key=lambda t: (
                len(set(t['metadata'].get('topic_tags', [])) & 
                    set(problem.get('topic_tags', []))),
                -abs(t['metadata'].get('acceptance_rate', 0) - 
                     problem.get('acceptance_rate', 0))
            ),
            reverse=True
        )
        
        selected = sorted_templates[0]
        
        # Track template usage
        if selected['template_id'] not in self.used_templates:
            self.used_templates[selected['template_id']] = set()
        self.used_templates[selected['template_id']].add(problem_id)
        
        return selected['content'], selected['metadata']

class ClaudeTestGenerator:
    """Generates test cases using Claude with template-based few-shot learning"""
    def __init__(self, dataset_path: Path, templates_path: Path):
        self.dataset_path = Path(dataset_path)
        if not self.dataset_path.exists():
            raise FileNotFoundError(f"Dataset path does not exist: {dataset_path}")
        
        parent_dir = self.dataset_path.parent.parent
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.output_path = parent_dir / "claude_generated_testcases"
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        self.template_manager = TestTemplate(templates_path)
        self._setup_logging(timestamp)
        
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        self.client = Anthropic(api_key=api_key)

    def _setup_logging(self, timestamp: str):
        """Setup logging configuration"""
        log_path = self.output_path / 'logs'
        log_path.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path / f'claude_generation_{timestamp}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _get_output_name(self, problem: Dict) -> str:
        """Generate concise output filename"""
        return f"claude_{problem['difficulty'].lower()}_{problem['problem_id']}"

    def _create_zero_shot_prompt(self, problem_content: str, template_content: str) -> str:
        """Create zero-shot prompt for test generation"""
        return f"""Generate pytest test cases for this Python LeetCode problem.

Problem Description:
{problem_content}

Python Template:
{template_content}

Requirements:
1. Create a TestSolution class to contain all test methods
2. Place the pytest.mark.parametrize decorator inside the TestSolution class
3. Include self parameter in test methods since they're class methods
4. Add proper type hints for all parameters
5. Include both basic test cases from the problem description and edge cases
6. Follow the exact import format from the template file
7. Match the test method name with the method in the template
8. Use assert statements to verify the solution
9. Initialize Solution class instance inside test methods

Generate only the test code without any explanations."""

    def _create_few_shot_prompt(self, problem_content: str, template_content: str, 
                              example_template: str, template_metadata: Dict) -> str:
        """Create few-shot prompt using category template"""
        return f"""Generate pytest test cases for this Python LeetCode problem.

Problem Description:
{problem_content}

Python Template:
{template_content}

Here is an example of the test structure to follow:
{example_template}

Requirements:
1. Structure your test exactly like the example test above
2. Follow the same TestSolution class pattern shown in the example
3. Create test cases that include:
   - Basic test cases from the problem description
   - Edge cases (empty inputs, boundary values, etc.)
   - Negative test cases where applicable
4. Technical requirements:
   - Use pytest.mark.parametrize decorator inside the class
   - Include self parameter in test methods
   - Add proper type hints for all parameters
   - Initialize Solution class instance inside test methods
   - Match the test method name with your template's method
5. Keep the same import structure as shown in the example

Generate only the test code without any explanations."""

    def _save_generated_test(self, output_name: str, test_content: str, 
                           shot_type: str, metadata: Dict, template_metadata: Optional[Dict] = None):
        """Save generated test with simplified naming"""
        output_dir = self.output_path / "problem_outputs" / f"{metadata['difficulty'].lower()}_{metadata['problem_id']}" / shot_type
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Clean test content
        test_content = test_content.strip()
        
        # Save test file
        test_file = output_dir / f"{output_name}_{shot_type}_test.py"
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        # Save metadata
        metadata_file = output_dir / f"{output_name}_{shot_type}_metadata.json"
        metadata_content = {
            'timestamp': datetime.now().isoformat(),
            'shot_type': shot_type,
            'problem_metadata': metadata,
            'model': 'claude-3-sonnet-20240229',
            'temperature': 0.2
        }
        if template_metadata and shot_type == 'few_shot':
            metadata_content['template_metadata'] = template_metadata
            
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata_content, f, indent=2)
            
        self.logger.info(f"Saved {shot_type} test to {output_dir}")

    def generate_test_cases(self, problem: Dict, shot_type: str = 'zero_shot') -> bool:
        """Generate test cases using specified strategy"""
        try:
            # Construct proper problem directory name
            problem_name = problem['title'].lower().replace(' ', '_').replace('-', '_')
            problem_dir_name = f"{problem['difficulty'].lower()}_{problem['problem_id']}_{problem_name}"
            problem_dir = self.dataset_path / problem_dir_name
            
            # Verify the problem directory exists
            if not problem_dir.exists():
                raise FileNotFoundError(f"Problem directory not found: {problem_dir}")
            
            # Construct and verify file paths
            problem_file = problem_dir / f"{problem_dir_name}_problem.md"
            template_file = problem_dir / f"{problem_dir_name}_template.py"
            
            if not problem_file.exists():
                raise FileNotFoundError(f"Problem file not found: {problem_file}")
            if not template_file.exists():
                raise FileNotFoundError(f"Template file not found: {template_file}")
            
            # Read problem files
            with open(problem_file, 'r', encoding='utf-8') as f:
                problem_content = f.read()
            
            with open(template_file, 'r', encoding='utf-8') as f:
                template_content = f.read()

            # Handle few-shot template selection
            example_template = ""
            template_metadata = {}
            if shot_type == 'few_shot':
                example_template, template_metadata = self.template_manager.get_template(problem)

            # Create appropriate prompt
            prompt = (self._create_few_shot_prompt(problem_content, template_content, example_template, template_metadata) 
                    if shot_type == 'few_shot' 
                    else self._create_zero_shot_prompt(problem_content, template_content))

            # Generate test cases with rate limiting
            self.logger.info(f"Using {shot_type} prompting for {problem['title']}")
            time.sleep(1)  # Basic rate limiting
            
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2000
            )
            
            test_content = response.content[0].text
            output_name = self._get_output_name(problem)
            
            # Save with template metadata for few-shot
            self._save_generated_test(
                output_name, 
                test_content, 
                shot_type, 
                problem,
                template_metadata if shot_type == 'few_shot' else None
            )
            
            # Log success
            self.logger.info(f"Successfully generated {shot_type} test cases for {problem['title']}")
            return True
                
        except FileNotFoundError as e:
            self.logger.error(f"File not found error for {problem['title']}: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Error generating test cases for {problem['title']}: {str(e)}")
            return False
            
def main():
    try:
        dataset_path = Path("dataset_leetcode/dataset_20241126_193530")
        templates_path = Path("templates_generation")
        
        if not dataset_path.exists() or not templates_path.exists():
            raise FileNotFoundError("Required directories not found")
            
        print(f"Using dataset directory: {dataset_path}")
        print(f"Using templates from: {templates_path}")
        
        generator = ClaudeTestGenerator(dataset_path, templates_path)
        
        with open(dataset_path / "baseline_report.json", 'r') as f:
            problems = json.load(f)['problems']
        
        for problem in problems:
            print(f"\nProcessing {problem['title']}...")
            
            for shot_type in ['zero_shot', 'few_shot']:
                print(f"{shot_type.title()} generation...")
                if generator.generate_test_cases(problem, shot_type):
                    print(f"{shot_type.title()} generation successful")
                else:
                    print(f"{shot_type.title()} generation failed")
            
            print(f"Completed test generation for {problem['title']}")
        
        print(f"\nGeneration complete! Tests saved in: {generator.output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()