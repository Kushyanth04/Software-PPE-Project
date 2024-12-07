import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1929_concatenation_of_array')
from easy_1929_concatenation_of_array_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
            ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
            ([1], [1, 1]),
            ([1000], [1000, 1000]),
            ([], []),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
        ],
    )
    def test_getConcatenation(self, nums: List[int], expected: List[int]) -> None:
        solution = Solution()
        assert solution.getConcatenation(nums) == expected