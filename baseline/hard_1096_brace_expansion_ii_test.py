from typing import List
import pytest
from hard_1096_brace_expansion_ii_solution import Solution


@pytest.mark.parametrize(
    "expression, output",
    [
        ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
        ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
    ],
)
class TestSolution:
    def test_braceExpansionII(self, expression: str, output: List[str]):
        sc = Solution()
        assert (
            sc.braceExpansionII(
                expression,
            )
            == output
        )
