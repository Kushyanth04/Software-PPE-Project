import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers')  
from medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "n, expected",
        [
            ("32", 3),
            ("82734", 8),
            ("27346209830709182346", 9),
            ("1", 1),
            ("11", 2),
            ("99999999999999999999999999999999999999999999999999999999999999999", 9),
        ],
    )
    def test_minPartitions(self, n: str, expected: int):
        solution = Solution()
        assert solution.minPartitions(n) == expected