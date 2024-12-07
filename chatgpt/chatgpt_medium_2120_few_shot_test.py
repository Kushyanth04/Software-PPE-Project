from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2120_execution_of_all_suffix_instructions_staying_in_a_grid')  
from medium_2120_execution_of_all_suffix_instructions_staying_in_a_grid_solution import Solution  

@pytest.mark.parametrize(
    "n, startPos, s, output",
    [
        (3, [0, 1], "RRDDLU", [1, 5, 4, 3, 1, 0]),
        (2, [1, 1], "LURD", [4, 1, 0, 0]),
        (1, [0, 0], "LRUD", [0, 0, 0, 0]),
        (5, [2, 2], "ULDR", [3, 2, 1, 0]),
        (4, [0, 0], "DDDD", [0]),
        (4, [3, 3], "UUUU", [0]),
        (4, [0, 0], "RRRR", [3]),
        (4, [0, 0], "LLLL", [0]),
        (4, [0, 0], "", [0]),
        (4, [0, 0], "R", [1]),
        (4, [3, 3], "L", [1]),
        (4, [3, 0], "U", [1]),
        (4, [0, 3], "D", [1])
    ]
)
class TestSolution:
    def test_executeInstructions(self, n: int, startPos: List[int], s: str, output: List[int]):
        sol = Solution()
        assert sol.executeInstructions(n, startPos, s) == output