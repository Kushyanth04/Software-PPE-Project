import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1096_brace_expansion_ii')
from hard_1096_brace_expansion_ii_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
            ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
            ("a", ["a"]),
            ("", []),
            ("{}", []),
            ("{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}{{}}")])
    def test_braceExpansionII(self, expression: str, expected: List[str]):
        sol = Solution()
        result = sol.braceExpansionII(expression)
        assert sorted(result) == sorted(expected), f"Failed for expression: {expression}"
