import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix')  
from hard_1284_minimum_number_of_flips_to_convert_binary_matrix_to_zero_matrix_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "mat, output",
        [
            ([[0, 0], [0, 1]], 3),
            ([[0]], 0),
            ([[1, 0, 0], [1, 0, 0]], -1),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 2),
            ([], -1),
            ([[]], 0),
        ],
    )
    def test_minFlips(self, mat: List[List[int]], output: int):
        sc = Solution()
        assert sc.minFlips(mat) == output