import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers')  
from medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers_solution import Solution  

@pytest.mark.parametrize(
    "n, expected_output",
    [
        ("32", 3),
        ("82734", 8),
        ("27346209830709182346", 9),
        ("0", 0),  # Edge case: single zero
        ("1", 1),  # Edge case: single one
        ("10", 1),  # Edge case: deci-binary number itself
        ("9999999999", 9),  # Edge case: all same digits
        ("1234567890", 9),  # Mixed digits
    ],
)
class TestSolution:
    def test_minPartitions(self, n: str, expected_output: int):
        solution = Solution()
        assert solution.minPartitions(n) == expected_output