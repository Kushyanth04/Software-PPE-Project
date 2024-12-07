import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_2392_build_a_matrix_with_conditions')  
from hard_2392_build_a_matrix_with_conditions_solution import Solution  

@pytest.mark.parametrize(
    "k, rowConditions, colConditions, expected_output",
    [
        (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
        (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], []),
        (2, [], [], [[1, 0], [0, 2]]),
        (4, [[1, 2], [3, 4]], [[2, 1], [4, 3]], [[4, 0, 0, 0], [0, 0, 2, 0], [0, 1, 0, 0], [0, 0, 0, 3]]),
        (400, [], [], [[i for i in range(1, 401)]] + [[0] * 399 for _ in range(399)]),
    ],
)
class TestSolution:
    def test_buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
        expected_output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.buildMatrix(k, rowConditions, colConditions) == expected_output
        )
