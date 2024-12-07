import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1096_brace_expansion_ii')
from hard_1096_brace_expansion_ii_solution import Solution  


@pytest.mark.parametrize(
    "expression, output",
    [
        ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
        ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
        ("a{}", []),
        ("{}{}", []),
        ("{{}}",  []),
        ("{{{}}}",  []),
        ("a{b,c}d", ["abd", "acd"]),
        ("{a,b,c}", ["a", "b", "c"]),
        ("{{a},{b,c}}", ["a", "b", "c"]),
        ("{{a,b},{c,d}}", ["a", "b", "c", "d"]),
        ("a{b,c}{d,e}f{g,h}", ["abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"]),
    ],
)
class TestSolution:
    def test_braceExpansionII(self, expression: str, output: List[str]):
        sc = Solution()
        assert sorted(sc.braceExpansionII(expression)) == sorted(output)
