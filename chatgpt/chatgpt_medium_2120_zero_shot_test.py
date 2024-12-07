from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2120_execution_of_all_suffix_instructions_staying_in_a_grid')  
from medium_2120_execution_of_all_suffix_instructions_staying_in_a_grid_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "n, startPos, s, expected",
        [
            (3, [0, 1], "RRDDLU", [1, 5, 4, 3, 1, 0]),
            (2, [1, 1], "LURD", [4, 1, 0, 0]),
            (1, [0, 0], "LRUD", [0, 0, 0, 0]),
            (5, [2, 2], "LURD", [3, 3, 3, 3]),
            (5, [4, 4], "DDDD", [0]),
            (5, [0, 0], "UUUU", [0]),
            (5, [0, 0], "LLLL", [0]),
            (5, [0, 0], "RRRR", [4]),
            (5, [0, 0], "DDDD", [4]),
            (5, [4, 4], "RRRR", [0]),
            (5, [4, 4], "UUUU", [4]),
            (5, [4, 4], "LLLL", [4]),
            (5, [4, 4], "DDDD", [0]),
            (5, [0, 4], "RRRR", [0]),
            (5, [0, 4], "UUUU", [0]),
            (5, [0, 4], "LLLL", [4]),
            (5, [0, 4], "DDDD", [4]),
            (5, [4, 0], "RRRR", [4]),
            (5, [4, 0], "UUUU", [4]),
            (5, [4, 0], "LLLL", [0]),
            (5, [4, 0], "DDDD", [0])
        ]
    )
    def test_executeInstructions(self, n: int, startPos: List[int], s: str, expected: List[int]):
        sol = Solution()
        result = sol.executeInstructions(n, startPos, s)
        assert result == expected