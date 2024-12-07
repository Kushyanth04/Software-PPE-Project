from typing import List
import pytest
from medium_2120_execution_of_all_suffix_instructions_staying_in_a_grid_solution import Solution


@pytest.mark.parametrize(
    "n, startPos, s, output",
    [
        (3, [0, 1], "RRDDLU", [1, 5, 4, 3, 1, 0]),
        (2, [1, 1], "LURD", [4, 1, 0, 0]),
        (1, [0, 0], "LRUD", [0, 0, 0, 0]),
    ],
)
class TestSolution:
    def test_executeInstructions(
        self, n: int, startPos: List[int], s: str, output: List[int]
    ):
        sc = Solution()
        assert (
            sc.executeInstructions(
                n,
                startPos,
                s,
            )
            == output
        )
