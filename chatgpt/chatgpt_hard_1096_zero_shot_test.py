import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1096_brace_expansion_ii')
from hard_1096_brace_expansion_ii_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize("expression, expected", [
        ("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be"]),
        ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z"]),
        ("a", ["a"]),
        ("{a,b,c}", ["a", "b", "c"]),
        ("{a,b}{c,d}", ["ac", "ad", "bc", "bd"]),
        ("a{b,c}{d,e}f{g,h}", ["abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"]),
        ("{{a},{a,b},{b,c}}", ["a", "b", "c"]),
        ("{x,y}{1,2}", ["x1", "x2", "y1", "y2"]),
        ("{a,b,c}{x,y}", ["ax", "ay", "bx", "by", "cx", "cy"]),
        ("{a,b,c}d", ["ad", "bd", "cd"]),
        ("{a,b,c}{d}", ["ad", "bd", "cd"]),
        ("z", ["z"]),
        ("{a}", ["a"]),
        ("{a,{a,b}}", ["a", "b"]),
        ("{a,b}{}", ["a", "b"]),
        ("{}{a,b}", ["a", "b"]),
        ("{a,b}{c,}", ["ac", "bc"]),
        ("{a,b}{,c}", ["a", "ac", "b", "bc"]),
        ("{a,b}{,}", ["a", "b"]),
        ("{,}{a,b}", ["a", "b"]),
        ("{,a}{b,}", ["b", "ab"]),
        ("{,}{,}", [""]),
        ("{a,b,c}{d,e,f}", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("{a,b,c}{d,e,f}g", ["adg", "aeg", "afg", "bdg", "beg", "bfg", "cdg", "ceg", "cfg"]),
        ("{a,b,c}{d,e,f}{g,h}", ["adg", "adh", "aeg", "aeh", "afg", "afh", "bdg", "bdh", "beg", "beh", "bfg", "bfh", "cdg", "cdh", "ceg", "ceh", "cfg", "cfh"])
    ])
    def test_braceExpansionII(self, expression: str, expected: List[str]):
        sol = Solution()
        result = sol.braceExpansionII(expression)
        assert sorted(result) == sorted(expected), f"Failed for expression: {expression}"