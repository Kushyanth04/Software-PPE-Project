from typing import List
import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2433_find_the_original_array_of_prefix_xor')  
from medium_2433_find_the_original_array_of_prefix_xor_solution import Solution  


@pytest.mark.parametrize(
    "pref, expected_output",
    [
        ([5, 2, 0, 3, 1], [5, 7, 2, 3, 2]),
        ([13], [13]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 3, 1, 7, 9]),
        ([10**6, 0, 10**6, 0], [10**6, 10**6, 0, 0]),
    ],
)
class TestSolution:
    def test_findArray(self, pref: List[int], expected_output: List[int]):
        sc = Solution()
        assert sc.findArray(pref) == expected_output

    def test_empty_input(self):
        sc = Solution()
        assert sc.findArray([]) == []

    def test_single_element(self):
        sc = Solution()
        assert sc.findArray([42]) == [42]

    def test_all_zeros(self):
        sc = Solution()
        assert sc.findArray([0] * 100) == [0] * 100

    def test_max_value(self):
        sc = Solution()
        assert sc.findArray([10**6] * 100) == [10**6] * 100
