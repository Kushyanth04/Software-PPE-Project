import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1512_number_of_good_pairs')
from easy_1512_number_of_good_pairs_solution import Solution 

class TestSolution:
    @pytest.mark.parametrize("nums, expected", [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([], 0),
        ([1], 0),
        ([1, 1], 1),
        ([100, 100, 100], 3),
        ([1, 2, 2, 3, 3, 3], 6),
        ([i for i in range(1, 101)], 0),  # worst case no pairs
        ([1] * 100, 4950)  # worst case all pairs
    ])
    def test_numIdenticalPairs(self, nums: List[int], expected: int):
        sol = Solution()
        assert sol.numIdenticalPairs(nums) == expected