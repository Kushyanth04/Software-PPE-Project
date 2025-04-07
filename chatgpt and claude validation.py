import pytest
import ast
import sys
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class TestValidator:
    def __init__(self, test_files: List[Path]):
        self.test_files = test_files
        self._setup_logging()
        
    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s: %(message)s',
            handlers=[
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def validate_syntax(self, file_path: Path) -> bool:
        """Validate Python syntax of test file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            return True
        except Exception as e:
            self.logger.error(f"Syntax error in {file_path.name}: {str(e)}")
            return False

    def validate_imports(self, file_path: Path) -> bool:
        """Validate required imports are present"""
        required_imports = {'pytest'}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            imports = set()
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        imports.add(name.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.add(node.module)
            
            missing = required_imports - imports
            if missing:
                self.logger.error(f"Missing imports in {file_path.name}: {missing}")
                return False
            return True
        except Exception:
            return False

    def validate_test_structure(self, file_path: Path) -> bool:
        """Validate pytest test structure"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            has_test_class = False
            has_test_method = False
            has_parametrize = False
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        has_test_class = True
                elif isinstance(node, ast.FunctionDef):
                    if node.name.startswith('test_'):
                        has_test_method = True
                elif isinstance(node, ast.Attribute):
                    if node.attr == 'parametrize':
                        has_parametrize = True
            
            if not (has_test_class and has_test_method and has_parametrize):
                missing = []
                if not has_test_class: missing.append("Test class")
                if not has_test_method: missing.append("test method")
                if not has_parametrize: missing.append("@pytest.mark.parametrize")
                self.logger.error(f"Missing in {file_path.name}: {', '.join(missing)}")
                return False
            return True
        except Exception as e:
            self.logger.error(f"Error in {file_path.name}: {str(e)}")
            return False

    def validate_test_file(self, file_path: Path):
        """Validate a single test file"""
        self.logger.info(f"\nValidating {file_path.name}")
        
        # Validate syntax
        if not self.validate_syntax(file_path):
            return False
        self.logger.info("[PASS] Syntax validation")
        
        # Validate imports
        if not self.validate_imports(file_path):
            return False
        self.logger.info("[PASS] Import validation")
        
        # Validate test structure
        if not self.validate_test_structure(file_path):
            return False
        self.logger.info("[PASS] Structure validation")
        
        return True

    def validate_all(self):
        """Validate all test files"""
        results = []
        for file_path in self.test_files:
            is_valid = self.validate_test_file(file_path)
            results.append((file_path.name, is_valid))
        
        print("\nValidation Summary:")
        print("-" * 50)
        for name, is_valid in results:
            status = "PASS" if is_valid else "FAIL"
            print(f"[{status}] {name}")

def main():
    # Sample test files - one from each category
    test_files = [
        # Easy - Jewels and Stones
        Path("chatgpt_generated_testcases/problem_outputs/easy_771_jewels_and_stones/chatgpt_zero_shot/chatgpt_easy_771_jewels_and_stones_zero_shot_test.py"),
        Path("claude_generated_testcases/problem_outputs/easy_771_jewels_and_stones/claude_zero_shot/claude_easy_771_jewels_and_stones_zero_shot_test.py"),
        
        # Medium - Sort Vowels in a String
        Path("chatgpt_generated_testcases/problem_outputs/medium_2785_sort_vowels_in_a_string/chatgpt_zero_shot/chatgpt_medium_2785_sort_vowels_in_a_string_zero_shot_test.py"),
        Path("claude_generated_testcases/problem_outputs/medium_2785_sort_vowels_in_a_string/claude_zero_shot/claude_medium_2785_sort_vowels_in_a_string_zero_shot_test.py"),
        
        # Hard - Orderly Queue
        Path("chatgpt_generated_testcases/problem_outputs/hard_899_orderly_queue/chatgpt_zero_shot/chatgpt_hard_899_orderly_queue_zero_shot_test.py"),
        Path("claude_generated_testcases/problem_outputs/hard_899_orderly_queue/claude_zero_shot/claude_hard_899_orderly_queue_zero_shot_test.py")
    ]
    
    # Verify files exist
    existing_files = [f for f in test_files if f.exists()]
    if not existing_files:
        print("Error: No test files found")
        sys.exit(1)
    
    validator = TestValidator(existing_files)
    validator.validate_all()

if __name__ == "__main__":
    main()