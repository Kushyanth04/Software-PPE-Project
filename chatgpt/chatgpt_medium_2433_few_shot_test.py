from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2433_find_the_original_array_of_prefix_xor')  
from medium_2433_find_the_original_array_of_prefix_xor_solution import Solution  

@pytest.mark.parametrize(
    "pref, output",
    [
        ([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]),
        ([13], [13]),
        ([0, 0, 0], [0, 0, 0]),  # All zeros in pref
        ([1, 0, 1, 0], [1, 1, 0, 1]),  # Alternating xor results
        ([0], [0]),  # Single zero element
        ([1], [1]),  # Single non-zero element
        ([2**20 - 1, 0], [2**20 - 1, 2**20 - 1]),  # Large numbers
    ],
)
class TestSolution:
    def test_findArray(self, pref: List[int], output: List[int]):
        sc = Solution()
        assert sc.findArray(pref) == output