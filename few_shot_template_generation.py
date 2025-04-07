import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class TemplateGenerator:
    def __init__(self):
        """Initialize template generator"""
        self.templates_base_path = Path("templates_generation")
        self.templates_base_path.mkdir(parents=True, exist_ok=True)

        self.output_path = self.templates_base_path / "generated_templates"
        self.output_path.mkdir(parents=True, exist_ok=True)

        self.used_templates = {}
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration"""
        log_path = self.templates_base_path / 'logs'
        log_path.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path / f'template_generation_{timestamp}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _get_clean_name(self, difficulty: str, problem_id: str, title: str) -> str:
        """Generate consistent file names"""
        return f"{difficulty.lower()}_{problem_id}_{title.lower().replace('-', '_').replace(' ', '_')}"

    def _validate_and_extract_test_content(self, template_file: Path) -> Optional[str]:
        """Validate and extract test content from file"""
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Ensure the file has a proper structure
            if "@pytest.mark.parametrize" not in content or "class TestSolution:" not in content:
                self.logger.warning(f"Invalid structure in file {template_file}")
                return None

            return content

        except Exception as e:
            self.logger.error(f"Error reading template file {template_file}: {str(e)}")
            return None

    def _prepare_template(self, template_content: str, category: str, template_problem: Dict) -> str:
        """Prepare the template with extracted content"""
        difficulty, prob_type = category.split()
        template = f'''"""
Template for {category} test cases, using {template_problem['title']} as example.
"""
{template_content}
"""
'''
        return template

    def generate_template(self, dataset_path: Path):
        """Generate templates using problems from baseline report"""
        try:
            with open(dataset_path / "baseline_report.json", 'r') as f:
                report = json.load(f)
            problems = report.get('problems', [])

            stats = {
                'Easy': {'array': 0, 'string': 0},
                'Medium': {'array': 0, 'string': 0},
                'Hard': {'array': 0, 'string': 0}
            }

            for problem in problems:
                difficulty = problem['difficulty']
                prob_type = problem['problem_type']
                problem_id = problem['problem_id']

                self.logger.info(f"Processing {problem['title']} ({difficulty} {prob_type})")

                template_problem = self._select_template_problem(
                    problems, difficulty, prob_type, problem_id
                )

                if not template_problem:
                    self.logger.warning(f"No suitable template found for {problem['title']}")
                    continue

                template_dir = self.output_path / f"{difficulty.lower()}_{prob_type}"
                template_dir.mkdir(exist_ok=True)

                template_name = self._get_clean_name(difficulty, problem_id, problem['title'])
                template_path = dataset_path / template_name
                test_files = list(template_path.glob('*_test.py'))

                if not test_files:
                    self.logger.error(f"Test file not found for template: {template_name}")
                    continue

                # Extract content from the original test file
                template_content = self._validate_and_extract_test_content(test_files[0])
                if not template_content:
                    self.logger.error(f"Failed to extract content from file: {test_files[0]}")
                    continue

                category = f"{difficulty} {prob_type}"
                prepared_template = self._prepare_template(template_content, category, template_problem)

                # Write template file
                output_file = template_dir / f"{difficulty.lower()}_{prob_type}_{problem_id}_template_test.py"
                with open(output_file, 'w', encoding='utf-8') as tf:
                    tf.write(prepared_template)

                # Write metadata file
                metadata_file = template_dir / f"{difficulty.lower()}_{prob_type}_{problem_id}_metadata.json"
                with open(metadata_file, 'w', encoding='utf-8') as mf:
                    json.dump({
                        'category': category,
                        'template_problem': template_problem['title'],
                        'target_problem': problem['title'],
                        'template_id': template_problem['problem_id'],
                        'target_id': problem['problem_id'],
                        'generation_timestamp': datetime.now().isoformat()
                    }, mf, indent=2)

                stats[difficulty][prob_type] += 1
                self.logger.info(f"Generated template for {problem['title']} using {template_problem['title']}")

            self.logger.info("\nTemplate Generation Statistics:")
            for diff, ptype_stats in stats.items():
                for ptype, count in ptype_stats.items():
                    self.logger.info(f"{diff} {ptype}: {count} templates")

            return True

        except Exception as e:
            self.logger.error(f"Error generating templates: {str(e)}")
            return False

    def _select_template_problem(self, problems: List[Dict], difficulty: str, problem_type: str, target_problem_id: str) -> Optional[Dict]:
        """Select a template problem based on criteria"""
        candidates = [
            p for p in problems if p['difficulty'] == difficulty and p['problem_type'] == problem_type
            and p['problem_id'] != target_problem_id
        ]

        if not candidates:
            return None

        return candidates[0]

    def print_directory_structure(self):
        """Print directory structure"""
        print("\nTemplate directory structure:")
        print("templates_generation/")
        print("|-- generated_templates/")
        for folder in self.output_path.iterdir():
            if folder.is_dir():
                print(f"|   |-- {folder.name}/")
                for file in folder.iterdir():
                    print(f"|   |   |-- {file.name}")
        print("+-- logs/")
        print("    +-- template_generation_TIMESTAMP.log")


def main():
    try:
        print("Starting template generation...")

        dataset_path = Path("dataset_leetcode/dataset_20241126_193530")
        if not dataset_path.exists():
            raise FileNotFoundError(f"Dataset not found at {dataset_path}")

        generator = TemplateGenerator()
        success = generator.generate_template(dataset_path)

        if success:
            print(f"\nTemplates generated successfully in: {generator.output_path}")
            generator.print_directory_structure()
        else:
            print("\nTemplate generation failed. Check logs for details.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
