from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2433_find_the_original_array_of_prefix_xor')  
from medium_2433_find_the_original_array_of_prefix_xor_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize("pref, expected", [
        ([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]),
        ([13], [13]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 3, 0], [1, 1, 2, 3]),
        ([2, 3], [2, 1]),
        ([0], [0]),
        ([1, 1, 1, 1], [1, 0, 0, 0])
    ])
    def test_findArray(self, pref: List[int], expected: List[int]):
        sol = Solution()
        assert sol.findArray(pref) == expected