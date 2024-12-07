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
            (4, [0, 0], "RRRRR", [5, 4, 3, 2, 1]),
            (5, [4, 4], "DDDDD", [5, 4, 3, 2, 1]),
            (10, [0, 0], "RRRRRRRRRRDDDDDDDDDD", [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
            (500, [499, 499], "LULULULULU", [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        ],
    )
    def test_executeInstructions(self, n: int, startPos: List[int], s: str, expected: List[int]):
        solution = Solution()
        assert solution.executeInstructions(n, startPos, s) == expected