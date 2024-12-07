from typing import List
import pytest
from hard_1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix_solution import Solution


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
