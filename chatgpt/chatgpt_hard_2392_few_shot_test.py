import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_2392_build_a_matrix_with_conditions')  
from hard_2392_build_a_matrix_with_conditions_solution import Solution  

@pytest.mark.parametrize(
    "k, rowConditions, colConditions, output",
    [
        (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
        (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], []),
        (2, [[1, 2]], [[1, 2]], [[1, 0], [0, 2]]),
        (4, [[1, 2], [3, 4]], [[1, 3], [2, 4]], [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]),
        (2, [[1, 2], [2, 1]], [], []),
        (2, [], [[1, 2], [2, 1]], []),
        (5, [[1, 2], [3, 4], [5, 1]], [[1, 3], [2, 4], [5, 2]], []),
        (2, [], [], [[1, 0], [0, 2]]),  # Minimal case with no conditions
        (400, [[1, 2]], [[1, 2]], []),  # Large k value with simple condition
    ]
)
class TestSolution:
    def test_buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]], output: List[List[int]]):
        sc = Solution()
        result = sc.buildMatrix(k, rowConditions, colConditions)
        if output:
            assert sorted([tuple(row) for row in result]) == sorted([tuple(row) for row in output])
        else:
            assert result == output