import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1512_number_of_good_pairs')
from easy_1512_number_of_good_pairs_solution import Solution 

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([], 0),  # Edge case: empty list
        ([1], 0),  # Edge case: single element
        ([1, 1], 1),  # Edge case: two identical elements
        ([1, 2], 0),  # Edge case: two different elements
        ([100] * 100, 4950),  # Boundary case: maximum length and value
    ],
)
class TestSolution:
    def test_numIdenticalPairs(self, nums: List[int], expected: int):
        sol = Solution()
        assert sol.numIdenticalPairs(nums) == expected