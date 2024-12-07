import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1512_number_of_good_pairs')
from easy_1512_number_of_good_pairs_solution import Solution 

class TestSolution:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1, 1, 3], 4),
            ([1, 1, 1, 1], 6),
            ([1, 2, 3], 0),
            ([1], 0),
            ([100] * 100, 4950),
            ([], 0),
        ],
    )
    def test_numIdenticalPairs(self, nums: List[int], expected: int):
        solution = Solution()
        assert solution.numIdenticalPairs(nums) == expected