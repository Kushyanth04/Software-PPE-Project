import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1929_concatenation_of_array')
from easy_1929_concatenation_of_array_solution import Solution 


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        pass


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([], []),
        ([1], [1, 1]),
        ([1000] * 1000, [1000] * 2000),
    ],
)
class TestSolution:
    def test_getConcatenation(self, nums: List[int], expected: List[int]):
        sc = Solution()
        assert sc.getConcatenation(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], None),
        (None, None),
        ([1, 2, "a"], None),
    ],
)
def test_getConcatenation_negative(nums, expected):
    sc = Solution()
    if expected is None:
        with pytest.raises(Exception):
            sc.getConcatenation(nums)
    else:
        assert sc.getConcatenation(nums) == expected