from typing import List
import pytest
from easy_1929_concatenation_of_array_solution import Solution


@pytest.mark.parametrize(
    "nums, output",
    [([1, 2, 1], [1, 2, 1, 1, 2, 1]), ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])],
)
class TestSolution:
    def test_getConcatenation(self, nums: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.getConcatenation(
                nums,
            )
            == output
        )
