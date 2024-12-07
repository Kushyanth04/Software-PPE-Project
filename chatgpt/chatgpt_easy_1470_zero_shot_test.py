import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1470_shuffle_the_array')
from easy_1470_shuffle_the_array_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize("nums, n, expected", [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ([1, 2, 1, 2], 2, [1, 2, 1, 2]),  # Test with minimal variation
        ([1000, 1000, 1000, 1000], 2, [1000, 1000, 1000, 1000]),  # Test with max values
        ([1, 1000, 500, 500], 2, [1, 500, 1000, 500]),  # Test with mixed values
    ])
    def test_shuffle(self, nums: List[int], n: int, expected: List[int]):
        sol = Solution()
        result = sol.shuffle(nums, n)
        assert result == expected