import os
import sys
import json
import pytest
import coverage
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, List
import warnings
warnings.filterwarnings('ignore')

class CoverageAnalyzer:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.baseline_dir = self.base_dir / "dataset_leetcode/dataset_20241126_193530"
        self.chatgpt_dir = self.base_dir / "chatgpt_generated_testcases/problem_outputs"
        self.claude_dir = self.base_dir / "claude_generated_testcases/problem_outputs"
        self.results = {}

    def run_coverage_for_test(self, test_file: str, solution_file: str) -> Dict:
        """Run coverage analysis for a specific test file"""
        try:
            cov = coverage.Coverage()
            cov.start()
            
            solution_dir = os.path.dirname(solution_file)
            if solution_dir not in sys.path:
                sys.path.append(solution_dir)
                
            # Suppress pytest output
            pytest.main(['-q', test_file, '--no-header', '--tb=no'])
            
            cov.stop()
            
            # Get coverage data for solution file only
            total = 0
            data = cov.get_data()
            for filename in data.measured_files():
                if solution_file in filename:
                    analysis = cov.analysis2(filename)
                    executed = len(set(analysis[1]) - set(analysis[2]))
                    total_lines = len(set(analysis[1]))
                    total = (executed / total_lines * 100) if total_lines > 0 else 0
            
            cov.erase()
            return {"coverage": round(total, 2), "status": "pass"}
            
        except Exception as e:
            if 'cov' in locals():
                cov.erase()
            return {"coverage": 0, "status": f"fail: {str(e)[:100]}"}

    def analyze_problem(self, problem_id: str, difficulty: str):
        """Analyze coverage for a specific problem"""
        problem_results = {
            "baseline": {"coverage": 0, "status": "fail"},
            "chatgpt_zero": {"coverage": 0, "status": "fail"},
            "chatgpt_few": {"coverage": 0, "status": "fail"},
            "claude_zero": {"coverage": 0, "status": "fail"},
            "claude_few": {"coverage": 0, "status": "fail"}
        }

        try:
            # Find problem folder
            problem_prefix = f"{difficulty.lower()}_{problem_id}_"
            problem_folders = [folder for folder in self.baseline_dir.iterdir() 
                             if folder.name.startswith(problem_prefix)]
            if not problem_folders:
                raise FileNotFoundError(f"No folder found for {difficulty}_{problem_id}")
            problem_folder = problem_folders[0]

            # Get file paths
            solution_file = str(problem_folder / f"{problem_folder.name}_solution.py")
            
            test_files = {
                "baseline": str(problem_folder / f"{problem_folder.name}_test.py"),
                "chatgpt_zero": str(self.chatgpt_dir / f"{difficulty.lower()}_{problem_id}/zero_shot/chatgpt_{difficulty.lower()}_{problem_id}_zero_shot_test.py"),
                "chatgpt_few": str(self.chatgpt_dir / f"{difficulty.lower()}_{problem_id}/few_shot/chatgpt_{difficulty.lower()}_{problem_id}_few_shot_test.py"),
                "claude_zero": str(self.claude_dir / f"{difficulty.lower()}_{problem_id}/zero_shot/claude_{difficulty.lower()}_{problem_id}_zero_shot_test.py"),
                "claude_few": str(self.claude_dir / f"{difficulty.lower()}_{problem_id}/few_shot/claude_{difficulty.lower()}_{problem_id}_few_shot_test.py")
            }

            # Run coverage for each test file
            for test_type, test_file in test_files.items():
                if os.path.exists(test_file) and os.path.exists(solution_file):
                    result = self.run_coverage_for_test(test_file, solution_file)
                    problem_results[test_type] = result

            self.results[f"{difficulty}_{problem_id}"] = problem_results
            
        except Exception as e:
            print(f"Error analyzing {difficulty}_{problem_id}: {str(e)[:100]}")

    def analyze_all_problems(self):
        """Analyze all problems"""
        problems = [
            ("771", "Easy"), ("1221", "Easy"), ("1470", "Easy"),
            ("1512", "Easy"), ("1929", "Easy"), ("2194", "Easy"),
            ("1282", "Medium"), ("1689", "Medium"), ("2044", "Medium"),
            ("2120", "Medium"), ("2433", "Medium"), ("2785", "Medium"),
            ("899", "Hard"), ("1096", "Hard"), ("1284", "Hard"),
            ("1312", "Hard"), ("1526", "Hard"), ("2392", "Hard")
        ]

        for problem_id, difficulty in problems:
            print(f"Analyzing {difficulty}_{problem_id}...", end=" ")
            self.analyze_problem(problem_id, difficulty)
            print("Done")

    def generate_comparison_report(self):
        """Generate comprehensive comparison report"""
        # Initialize statistics
        stats = {
            'baseline': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'count': 0},
            'chatgpt_zero': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'count': 0},
            'chatgpt_few': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'count': 0},
            'claude_zero': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'count': 0},
            'claude_few': {'passed': 0, 'failed': 0, 'total_coverage': 0, 'count': 0}
        }
        
        difficulty_stats = {
            'Easy': {'baseline': [], 'chatgpt_zero': [], 'chatgpt_few': [], 'claude_zero': [], 'claude_few': []},
            'Medium': {'baseline': [], 'chatgpt_zero': [], 'chatgpt_few': [], 'claude_zero': [], 'claude_few': []},
            'Hard': {'baseline': [], 'chatgpt_zero': [], 'chatgpt_few': [], 'claude_zero': [], 'claude_few': []}
        }

        # Process results
        for problem_id, results in self.results.items():
            difficulty = problem_id.split('_')[0]
            
            for test_type in stats.keys():
                if test_type in results:
                    result = results[test_type]
                    stats[test_type]['count'] += 1
                    if result['status'] == 'pass':
                        stats[test_type]['passed'] += 1
                    else:
                        stats[test_type]['failed'] += 1
                    stats[test_type]['total_coverage'] += result['coverage']
                    difficulty_stats[difficulty][test_type].append(result['coverage'])

        # Print report
        print("\n" + "="*50)
        print("COVERAGE ANALYSIS REPORT")
        print("="*50)

        # Overall Results
        print("\nOverall Results:")
        print("-" * 80)
        print(f"{'Category':<15} {'Total':>8} {'Passed':>8} {'Failed':>8} {'Coverage %':>15}")
        print("-" * 80)
        
        for test_type, data in stats.items():
            if data['count'] > 0:
                avg_coverage = data['total_coverage'] / data['count']
                print(f"{test_type:<15} {data['count']:>8} {data['passed']:>8} "
                      f"{data['failed']:>8} {avg_coverage:>15.2f}")

        # Difficulty-wise Results
        print("\nDifficulty-wise Results:")
        print("-" * 80)
        print(f"{'Difficulty':<10} {'Category':<15} {'Coverage %':>15}")
        print("-" * 80)
        
        for diff in difficulty_stats:
            for test_type in stats:
                coverages = difficulty_stats[diff][test_type]
                if coverages:
                    avg_coverage = sum(coverages) / len(coverages)
                    print(f"{diff:<10} {test_type:<15} {avg_coverage:>15.2f}")

        # Save results
        self._save_results(stats, difficulty_stats)
        self._create_visualizations(stats, difficulty_stats)

    def _save_results(self, stats: Dict, difficulty_stats: Dict):
        """Save analysis results to JSON"""
        with open('coverage_analysis.json', 'w') as f:
            json.dump({
                'overall_stats': stats,
                'difficulty_stats': difficulty_stats
            }, f, indent=2)

    def _create_visualizations(self, stats: Dict, difficulty_stats: Dict):
        """Create visualization plots"""
        plt.style.use('seaborn')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # Overall Coverage Plot
        categories = list(stats.keys())
        coverages = [stats[cat]['total_coverage']/stats[cat]['count'] 
                    if stats[cat]['count'] > 0 else 0 for cat in categories]
        
        ax1.bar(categories, coverages)
        ax1.set_title('Overall Coverage by Test Category')
        ax1.set_ylabel('Average Coverage (%)')
        plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

        # Difficulty-wise Plot
        difficulties = list(difficulty_stats.keys())
        x = np.arange(len(difficulties))
        width = 0.15
        
        for i, category in enumerate(categories):
            coverages = []
            for diff in difficulties:
                values = difficulty_stats[diff][category]
                avg = sum(values)/len(values) if values else 0
                coverages.append(avg)
            ax2.bar(x + i*width, coverages, width, label=category)

        ax2.set_title('Coverage by Difficulty Level')
        ax2.set_ylabel('Average Coverage (%)')
        ax2.set_xticks(x + width*2)
        ax2.set_xticklabels(difficulties)
        ax2.legend()

        plt.tight_layout()
        plt.savefig('coverage_analysis.png')

def main():
    base_dir = r"C:\Users\kushy\Desktop\SE_PROJECT - Main"  
    analyzer = CoverageAnalyzer(base_dir)
    analyzer.analyze_all_problems()
    analyzer.generate_comparison_report()

if __name__ == "__main__":
    main()