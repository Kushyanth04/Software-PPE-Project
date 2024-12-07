import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1526_minimum_number_of_increments_on_subarrays_to_form_a_target_array')  
from hard_1526_minimum_number_of_increments_on_subarrays_to_form_a_target_array_solution import Solution  

@pytest.mark.parametrize(
    "target, output",
    [
        ([1, 2, 3, 2, 1], 3),
        ([3, 1, 1, 2], 4),
        ([3, 1, 5, 4, 2], 7),
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
    ],
)
class TestSolution:
    def test_minNumberOperations(self, target: List[int], output: int):
        sc = Solution()
        assert sc.minNumberOperations(target) == output

    @pytest.mark.parametrize("target", [[0], [-1], [0, 0]])
    def test_invalid_input(self, target: List[int]):
        sc = Solution()
        with pytest.raises(Exception):
            sc.minNumberOperations(target)