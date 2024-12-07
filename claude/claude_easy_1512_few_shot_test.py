import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1512_number_of_good_pairs')
from easy_1512_number_of_good_pairs_solution import Solution 


@pytest.mark.parametrize(
    "nums, expected_output",
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([], 0),
        ([1], 0),
        ([1, 1], 1),
        ([100] * 100, 4950),
    ],
)
class TestSolution:
    def test_numIdenticalPairs(self, nums: List[int], expected_output: int):
        sc = Solution()
        assert sc.numIdenticalPairs(nums) == expected_output


@pytest.mark.parametrize(
    "nums, expected_output",
    [
        ([101, 102, 103], 0),
        ([-1, -2, -3], 0),
    ],
)
class TestSolutionNegativeCases:
    def test_numIdenticalPairs(self, nums: List[int], expected_output: int):
        sc = Solution()
        assert sc.numIdenticalPairs(nums) == expected_output
