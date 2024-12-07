from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2044_count_number_of_maximum_bitwise_or_subsets')  
from medium_2044_count_number_of_maximum_bitwise_or_subsets_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize("nums, expected", [
        ([3, 1], 2),
        ([2, 2, 2], 7),
        ([3, 2, 1, 5], 6),
        ([1], 1),
        ([1, 1, 1, 1], 15),
        ([1, 2, 4, 8], 1),
        ([1, 2, 4, 8, 16], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8], 1),
        ([100000], 1),
        ([1, 100000], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 1)
    ])
    def test_countMaxOrSubsets(self, nums: List[int], expected: int):
        sol = Solution()
        assert sol.countMaxOrSubsets(nums) == expected