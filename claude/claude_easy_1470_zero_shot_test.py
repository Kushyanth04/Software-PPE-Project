import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1470_shuffle_the_array')
from easy_1470_shuffle_the_array_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "nums, n, expected",
        [
            ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
            ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
            ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
            ([1] * 1000, 500, [1] * 1000),  # Edge case: Large input
            ([], 0, []),  # Edge case: Empty input
            ([1, 2], 1, [1, 2]),  # Edge case: n = 1
        ],
    )
    def test_shuffle(self, nums: List[int], n: int, expected: List[int]) -> None:
        solution = Solution()
        assert solution.shuffle(nums, n) == expected