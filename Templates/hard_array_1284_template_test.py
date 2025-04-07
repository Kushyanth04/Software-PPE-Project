"""
Template for Hard array test cases, using Build a Matrix With Conditions as example.
"""
import pytest
from q_1284_minimumNumberOfFlipsToConvertBinaryMatrixToZeroMatrix import Solution


@pytest.mark.parametrize(
    "mat, output", [([[0, 0], [0, 1]], 3), ([[0]], 0), ([[1, 0, 0], [1, 0, 0]], -1)]
)
class TestSolution:
    def test_minFlips(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minFlips(
                mat,
            )
            == output
        )

"""
