import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1470_shuffle_the_array')
from easy_1470_shuffle_the_array_solution import Solution  

@pytest.mark.parametrize(
    "nums, n, expected",
    [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
        ([], 0, []),  # Edge case: empty input
        ([1, 2], 1, [1, 2]),  # Minimum valid input
        ([i for i in range(1, 1001)], 500, [i for j in range(500) for i in (j+1, j+501)])  # Large input case
    ]
)
class TestSolution:
    def test_shuffle(self, nums: List[int], n: int, expected: List[int]):
        sc = Solution()
        assert sc.shuffle(nums, n) == expected