import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_2392_build_a_matrix_with_conditions')  
from hard_2392_build_a_matrix_with_conditions_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "k, rowConditions, colConditions, expected",
        [
            (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
            (3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]], []),
            (2, [[1, 2]], [[1, 2]], [[1, 0], [0, 2]]),
            (4, [[1, 2], [3, 4]], [[1, 3], [2, 4]], [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]),
            (2, [[1, 2]], [[2, 1]], []),  # Impossible due to conflicting conditions
            (5, [], [], [[1, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 5]]),  # No conditions
        ]
    )
    def test_buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]], expected: List[List[int]]):
        sol = Solution()
        result = sol.buildMatrix(k, rowConditions, colConditions)
        assert result == expected or self._validate_matrix(k, rowConditions, colConditions, result)

    def _validate_matrix(self, k, rowConditions, colConditions, matrix):
        if not matrix:
            return False
        if len(matrix) != k or len(matrix[0]) != k:
            return False
        
        position = {}
        for i in range(k):
            for j in range(k):
                if matrix[i][j] != 0:
                    position[matrix[i][j]] = (i, j)
        
        for above, below in rowConditions:
            if above not in position or below not in position:
                return False
            if position[above][0] >= position[below][0]:
                return False
        
        for left, right in colConditions:
            if left not in position or right not in position:
                return False
            if position[left][1] >= position[right][1]:
                return False
        
        return True