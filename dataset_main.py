from importlib import metadata
import json
import time
import shutil
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from leetscrape import GetQuestionsList, GetQuestion, GenerateCodeStub
import pandas as pd
import logging
from datetime import datetime
from typing import List, Dict

@dataclass
class TestCaseStats:
    """Statistics about collected test cases"""
    total_test_cases: int = 0
    has_parametrized_tests: bool = False
    test_file_content: str = ""

@dataclass
class ProblemMetadata:
    """Metadata for collected problems"""
    problem_id: str
    title: str
    difficulty: str
    acceptance_rate: float
    topic_tags: list
    test_stats: TestCaseStats = None
    collection_timestamp: str = None
    problem_type: str = ''

class LeetCodeBaselineCollector:
    def __init__(self):
        """Initialize the collector with balanced type criteria"""
        self.criteria = {
            'Easy': {'array': 3, 'string': 3},
            'Medium': {'array': 3, 'string': 3},
            'Hard': {'array': 3, 'string': 3}
        }
        self.acceptance_rate_criteria = {'Easy': 70, 'Medium': 50, 'Hard': 30}
        self.base_path = Path("dataset_leetcode")
        self.base_path.mkdir(exist_ok=True)
        self.collected_stats = {
            'Easy': {'array': 0, 'string': 0},
            'Medium': {'array': 0, 'string': 0},
            'Hard': {'array': 0, 'string': 0}
        }
        self._setup_logging()

    def _setup_logging(self):
        """Setup logging configuration"""
        log_path = self.base_path / 'collection_logs'
        log_path.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path / f'collection_{timestamp}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _format_file_prefix(self, difficulty: str, problem_id: str, title_slug: str) -> str:
        """Generate consistent file prefix"""
        formatted_title = title_slug.replace('-', '_')
        return f"{difficulty.lower()}_{problem_id}_{formatted_title}"

    def _get_file_path(self, problem_dir: Path, prefix: str, file_type: str) -> Path:
        """Get consistent file path"""
        return problem_dir / f"{prefix}_{file_type}"

    def fetch_problems(self):
        """Fetch problems from LeetCode with type information"""
        self.logger.info("Fetching problems list...")
        questions_list = GetQuestionsList()
        questions_list.scrape()
        df = questions_list.questions

        # Print available columns for debugging
        self.logger.info(f"Available columns: {df.columns.tolist()}")

        # Add problem type classification
        df['is_array'] = df['topicTags'].apply(
            lambda x: 'array' in x.lower() and 'string' not in x.lower()
        )
        df['is_string'] = df['topicTags'].apply(
            lambda x: 'string' in x.lower() and 'array' not in x.lower()
        )
        
        # Classify problem type
        df['problem_type'] = 'other'
        df.loc[df['is_array'], 'problem_type'] = 'array'
        df.loc[df['is_string'], 'problem_type'] = 'string'
        
        return df

    def select_problems(self, df):
        """Select problems meeting criteria"""
        selected_problems = []
        
        for difficulty in ['Easy', 'Medium', 'Hard']:
            for prob_type in ['array', 'string']:
                remaining = (self.criteria[difficulty][prob_type] - 
                            self.collected_stats[difficulty][prob_type])
                
                if remaining <= 0:
                    continue

                self.logger.info(f"\nSelecting {difficulty} {prob_type} problems ({remaining} needed)...")
                
                # Filter problems based on criteria
                problems = df[
                    (df['difficulty'] == difficulty) &
                    (df['problem_type'] == prob_type) &
                    (~df['paidOnly']) &
                    (df['acceptanceRate'] > self.acceptance_rate_criteria[difficulty])
                ]
                
                # Sort by acceptance rate
                problems = problems.sort_values(by='acceptanceRate', ascending=False)
                
                selected = problems.head(remaining * 4)  # Get extras in case some fail
                if not selected.empty:
                    selected_problems.append(selected)
                else:
                    self.logger.warning(f"No {prob_type} problems found for difficulty {difficulty}")
        
        if not selected_problems:
            raise ValueError("No problems meeting criteria found")
            
        return pd.concat(selected_problems) if selected_problems else pd.DataFrame()

    def validate_test_file(self, test_file_path):
        """Validate LeetCode test file"""
        test_stats = TestCaseStats()
        
        if not test_file_path.exists():
            return test_stats

        with open(test_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            test_stats.test_file_content = content

            # Find parametrize decorators and their test cases
            parametrize_pattern = r'@pytest\.mark\.parametrize\([^[]*(\[.*?\])\s*\)'
            matches = re.findall(parametrize_pattern, content, re.DOTALL)
            
            if matches:
                test_stats.has_parametrized_tests = True
                for match in matches:
                    try:
                        # Count individual test cases in each parametrize
                        test_cases = eval(match)
                        test_stats.total_test_cases += len(test_cases)
                    except:
                        # If eval fails, count commas between parentheses
                        case_count = len(re.findall(r'\([^)]+\)', match))
                        test_stats.total_test_cases += max(case_count, 1)

        return test_stats

    def process_problem(self, problem, dataset_dir):
        """Process individual problem and collect baseline test cases"""
        prefix = self._format_file_prefix(
            problem['difficulty'],
            problem['QID'],
            problem['titleSlug']
        )
        problem_dir = dataset_dir / prefix
        problem_dir.mkdir(exist_ok=True)
        
        prob_type = problem['problem_type']
        difficulty = problem['difficulty']
        
        self.logger.info(f"\n{'='*80}")
        self.logger.info(f"Processing {difficulty} {prob_type} Problem: {problem['title']}")
        self.logger.info(f"Acceptance Rate: {problem['acceptanceRate']:.2f}%")
        
        try:
            # Get problem details
            question = GetQuestion(titleSlug=problem['titleSlug']).scrape()
            
            # Generate code stub and test file
            stub_gen = GenerateCodeStub(titleSlug=problem['titleSlug'])
            stub_gen.generate()
            
            # Move generated files with new naming
            for stub_file in Path().glob("q_*.py"):
                shutil.move(stub_file, self._get_file_path(problem_dir, prefix, "template.py"))
            for test_file in Path().glob("test_q_*.py*"):
                shutil.move(test_file, self._get_file_path(problem_dir, prefix, "test.py"))

            # Validate test file
            test_stats = self.validate_test_file(self._get_file_path(problem_dir, prefix, "test.py"))
            
            if not test_stats.has_parametrized_tests:
                raise ValueError("No valid test cases found")

            # Files successfully generated
            self.logger.info("SUCCESS: Generated Files:")
            self.logger.info(f"  - {prefix}_template.py")
            self.logger.info(f"  - {prefix}_test.py")
            self.logger.info(f"  - {prefix}_metadata.json")
            self.logger.info(f"  - {prefix}_problem.md")
            self.logger.info(f"  - {prefix}_test_cases.json")
            self.logger.info(f"Test Cases Found: {test_stats.total_test_cases}")

            # Create metadata
            metadata = ProblemMetadata(
                problem_id=problem['QID'],
                title=problem['title'],
                difficulty=problem['difficulty'],
                acceptance_rate=problem['acceptanceRate'],
                topic_tags=problem['topicTags'].split(','),
                test_stats=test_stats,
                collection_timestamp=datetime.now().isoformat(),
                problem_type=prob_type
            )

            # Save files with new naming convention
            with open(self._get_file_path(problem_dir, prefix, "metadata.json"), 'w', encoding='utf-8') as f:
                json.dump(asdict(metadata), f, indent=2)
            
            with open(self._get_file_path(problem_dir, prefix, "problem.md"), 'w', encoding='utf-8') as f:
                f.write(getattr(question, 'Body', ''))

            # Save test cases
            test_cases = self._extract_test_details(test_stats.test_file_content)
            with open(self._get_file_path(problem_dir, prefix, "test_cases.json"), 'w', encoding='utf-8') as f:
                json.dump({
                    'problem_id': problem['QID'],
                    'total_test_cases': test_stats.total_test_cases,
                    'test_cases': test_cases
                }, f, indent=2)

            # Update collection stats by type
            self.collected_stats[difficulty][prob_type] += 1
            self.logger.info(f"SUCCESS: Collected {problem['title']}")
            return metadata

        except Exception as e:
            self.logger.error(f"FAILED: {str(e)}")
            self.logger.info(f"Skipping {problem['title']}, will try next problem")
            if problem_dir.exists():
                shutil.rmtree(problem_dir)
            return None
    
    def _extract_test_details(self, content: str) -> List[Dict]:
        """Extract detailed test case information"""
        test_cases = []
        
        try:
            # Find parametrize blocks
            pattern = r'@pytest\.mark\.parametrize\([^[]*(\[.*?\])\s*\)'
            matches = re.findall(pattern, content, re.DOTALL)
            
            for match in matches:
                try:
                    cases = eval(match)
                    for case in cases:
                        if isinstance(case, tuple):
                            test_cases.append({
                                'inputs': list(case[:-1]),
                                'expected_output': case[-1],
                                'raw_case': str(case)
                            })
                except:
                    # If parsing fails, store raw test case
                    test_cases.append({
                        'raw_case': match.strip()
                    })
                    
        except Exception as e:
            self.logger.warning(f"Error extracting test details: {str(e)}")
            
        return test_cases

    def generate_collection_report(self, dataset_dir, collected_metadata):
        """Generate report with detailed type distribution"""
        total = 0
        for difficulty in self.collected_stats:
            for prob_type in self.collected_stats[difficulty]:
                total += self.collected_stats[difficulty][prob_type]

        report = {
            "timestamp": datetime.now().isoformat(),
            "total_problems": total,
            "distribution": {
                difficulty: {
                    "array": self.collected_stats[difficulty]['array'],
                    "string": self.collected_stats[difficulty]['string'],
                    "total": self.collected_stats[difficulty]['array'] + 
                            self.collected_stats[difficulty]['string']
                }
                for difficulty in self.collected_stats
            },
            "problems": [asdict(meta) for meta in collected_metadata if meta]
        }

        with open(dataset_dir / "baseline_report.json", 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        return report

    def collect_dataset(self):
            """Main collection method"""
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dataset_dir = self.base_path / f"dataset_{timestamp}"
            dataset_dir.mkdir(parents=True, exist_ok=True)

            collected_metadata = []
            try:
                df = self.fetch_problems()
                selected_problems = self.select_problems(df)

                for difficulty in ['Easy', 'Medium', 'Hard']:
                    self.logger.info(f"\n{'='*80}")
                    self.logger.info(f"Starting {difficulty} Problems Collection")
                    
                    for prob_type in ['array', 'string']:
                        target = self.criteria[difficulty][prob_type]
                        self.logger.info(f"\nTarget: {target} {difficulty} {prob_type} problems")
                        self.logger.info(f"Acceptance Rate Criterion: >{self.acceptance_rate_criteria[difficulty]}%")
                        
                        type_problems = selected_problems[
                            (selected_problems['difficulty'] == difficulty) & 
                            (selected_problems['problem_type'] == prob_type)
                        ]
                        attempted = 0
                        
                        while (self.collected_stats[difficulty][prob_type] < target and 
                            attempted < len(type_problems)):
                            
                            problem = type_problems.iloc[attempted]
                            metadata = self.process_problem(problem, dataset_dir)
                            
                            if metadata:
                                collected_metadata.append(metadata)
                                self.logger.info(
                                    f"Progress: {self.collected_stats[difficulty][prob_type]}/"
                                    f"{target} {difficulty} {prob_type} problems"
                                )
                            
                            attempted += 1
                        
                        if self.collected_stats[difficulty][prob_type] < target:
                            self.logger.warning(
                                f"Note: Could not find enough valid {difficulty} {prob_type} problems"
                            )

                report = self.generate_collection_report(dataset_dir, collected_metadata)
                
                # At the end of the method, update the summary logging:
                self.logger.info("\n" + "="*80)
                self.logger.info("Final Collection Summary:")
                total_problems = sum(
                    self.collected_stats[diff][ptype]
                    for diff in self.collected_stats 
                    for ptype in self.collected_stats[diff]
                )
                self.logger.info(f"Total Problems: {total_problems}/18")
                self.logger.info("Distribution:")
                for diff in ['Easy', 'Medium', 'Hard']:
                    self.logger.info(f"  - {diff}:")
                    for prob_type in ['array', 'string']:
                        self.logger.info(
                            f"    {prob_type}: {self.collected_stats[diff][prob_type]}/"
                            f"{self.criteria[diff][prob_type]}"
                        )
                self.logger.info(f"Dataset Location: {dataset_dir}")
                
                return dataset_dir

            except Exception as e:
                self.logger.error(f"Collection Error: {str(e)}")
                raise

def main():
    collector = LeetCodeBaselineCollector()
    try:
        dataset_dir = collector.collect_dataset()
        print(f"\nDataset collection complete. Saved at {dataset_dir}")
    except Exception as e:
        print(f"Error in dataset collection: {str(e)}")

if __name__ == "__main__":
    main()