from typing import List
import pytest
from easy_1470_shuffle_the_array_solution import Solution


@pytest.mark.parametrize(
    "nums, n, output",
    [
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
    ],
)
class TestSolution:
    def test_shuffle(self, nums: List[int], n: int, output: List[int]):
        sc = Solution()
        assert (
            sc.shuffle(
                nums,
                n,
            )
            == output
        )
