from typing import List
import pytest
from medium_2044_count_number_of_maximum_bitwise_or_subsets_solution import Solution


@pytest.mark.parametrize(
    "nums, output", [([3, 1], 2), ([2, 2, 2], 7), ([3, 2, 1, 5], 6)]
)
class TestSolution:
    def test_countMaxOrSubsets(self, nums: List[int], output: int):
        sc = Solution()
        assert (
            sc.countMaxOrSubsets(
                nums,
            )
            == output
        )
