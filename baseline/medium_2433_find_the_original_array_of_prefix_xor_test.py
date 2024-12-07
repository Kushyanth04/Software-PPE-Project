from typing import List
import pytest
from medium_2433_find_the_original_array_of_prefix_xor_solution import Solution


@pytest.mark.parametrize(
    "pref, output", [([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]), ([13], [13])]
)
class TestSolution:
    def test_findArray(self, pref: List[int], output: List[int]):
        sc = Solution()
        assert (
            sc.findArray(
                pref,
            )
            == output
        )
