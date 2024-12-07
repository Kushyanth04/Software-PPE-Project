import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers')  
from medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers_solution import Solution  


class TestSolution:
    @pytest.mark.parametrize("n, expected", [
        ("32", 3),
        ("82734", 8),
        ("27346209830709182346", 9),
        ("1", 1),
        ("10", 1),
        ("1111111111", 1),
        ("9999999999", 9),
        ("1234567890", 9),
        ("5050505050", 5)
    ])
    def test_minPartitions(self, n: str, expected: int):
        sol = Solution()
        assert sol.minPartitions(n) == expected