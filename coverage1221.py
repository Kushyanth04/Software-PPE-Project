import os
import sys
import pytest
import coverage
from pathlib import Path

def run_coverage_for_test(test_file_path: str, solution_path: str) -> dict:
    """Run coverage analysis for a specific test file"""
    cov = coverage.Coverage()
    cov.start()
    
    # Add solution directory to path so imports work
    solution_dir = os.path.dirname(solution_path)
    if solution_dir not in sys.path:
        sys.path.append(solution_dir)
    
    # Run pytest with the specific test file
    pytest.main(['-v', test_file_path])
    
    cov.stop()
    
    # Get coverage data
    total = cov.report()
    
    # Get line coverage details
    coverage_analysis = {}
    for filename in cov.get_data().measured_files():
        if solution_path in filename:
            analysis = cov.analysis2(filename)
            coverage_analysis = {
                'total_coverage': total,
                'executable_lines': set(analysis[1]),
                'missing_lines': set(analysis[2]),
                'covered_lines': set(analysis[1]) - set(analysis[2])
            }
    
    # Clean up coverage data
    cov.erase()
    
    return coverage_analysis

def main():
    # Define paths
    base_dir = Path(r"C:\Users\kushy\Desktop\SE_PROJECT - Main")
    
    # Solution file path
    solution_path = str(base_dir / "dataset_leetcode" / "dataset_20241126_193530" / 
                       "easy_1221_split_a_string_in_balanced_strings" / 
                       "easy_1221_split_a_string_in_balanced_strings_solution.py")
    
    # Test file paths
    baseline_test = str(base_dir / "dataset_leetcode" / "dataset_20241126_193530" / 
                       "easy_1221_split_a_string_in_balanced_strings" / 
                       "easy_1221_split_a_string_in_balanced_strings_test.py")
    
    # ChatGPT test paths
    chatgpt_zero_shot = str(base_dir / "chatgpt_generated_testcases" / "problem_outputs" / 
                           "easy_1221" / "zero_shot" / "chatgpt_easy_1221_zero_shot_test.py")
    chatgpt_few_shot = str(base_dir / "chatgpt_generated_testcases" / "problem_outputs" / 
                          "easy_1221" / "few_shot" / "chatgpt_easy_1221_few_shot_test.py")
    
    # Claude test paths
    claude_zero_shot = str(base_dir / "claude_generated_testcases" / "problem_outputs" / 
                          "easy_1221" / "zero_shot" / "claude_easy_1221_zero_shot_test.py")
    claude_few_shot = str(base_dir / "claude_generated_testcases" / "problem_outputs" / 
                         "easy_1221" / "few_shot" / "claude_easy_1221_few_shot_test.py")
    
    # Run coverage analysis for each test file
    print("Running coverage analysis...")
    
    print("\nBaseline Dataset Test Coverage:")
    baseline_coverage = run_coverage_for_test(baseline_test, solution_path)
    print(f"Total coverage: {baseline_coverage['total_coverage']:.2f}%")
    print(f"Executable lines: {sorted(baseline_coverage['executable_lines'])}")
    print(f"Covered lines: {sorted(baseline_coverage['covered_lines'])}")
    print(f"Missing lines: {sorted(baseline_coverage['missing_lines'])}")
    
    print("\nChatGPT Zero-Shot Test Coverage:")
    chatgpt_zero_coverage = run_coverage_for_test(chatgpt_zero_shot, solution_path)
    print(f"Total coverage: {chatgpt_zero_coverage['total_coverage']:.2f}%")
    print(f"Executable lines: {sorted(chatgpt_zero_coverage['executable_lines'])}")
    print(f"Covered lines: {sorted(chatgpt_zero_coverage['covered_lines'])}")
    print(f"Missing lines: {sorted(chatgpt_zero_coverage['missing_lines'])}")
    
    print("\nChatGPT Few-Shot Test Coverage:")
    chatgpt_few_coverage = run_coverage_for_test(chatgpt_few_shot, solution_path)
    print(f"Total coverage: {chatgpt_few_coverage['total_coverage']:.2f}%")
    print(f"Executable lines: {sorted(chatgpt_few_coverage['executable_lines'])}")
    print(f"Covered lines: {sorted(chatgpt_few_coverage['covered_lines'])}")
    print(f"Missing lines: {sorted(chatgpt_few_coverage['missing_lines'])}")
    
    print("\nClaude Zero-Shot Test Coverage:")
    claude_zero_coverage = run_coverage_for_test(claude_zero_shot, solution_path)
    print(f"Total coverage: {claude_zero_coverage['total_coverage']:.2f}%")
    print(f"Executable lines: {sorted(claude_zero_coverage['executable_lines'])}")
    print(f"Covered lines: {sorted(claude_zero_coverage['covered_lines'])}")
    print(f"Missing lines: {sorted(claude_zero_coverage['missing_lines'])}")
    
    print("\nClaude Few-Shot Test Coverage:")
    claude_few_coverage = run_coverage_for_test(claude_few_shot, solution_path)
    print(f"Total coverage: {claude_few_coverage['total_coverage']:.2f}%")
    print(f"Executable lines: {sorted(claude_few_coverage['executable_lines'])}")
    print(f"Covered lines: {sorted(claude_few_coverage['covered_lines'])}")
    print(f"Missing lines: {sorted(claude_few_coverage['missing_lines'])}")

if __name__ == "__main__":
    main()