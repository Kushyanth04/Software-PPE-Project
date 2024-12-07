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
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([5], 5),
        ([1, 3, 5, 7], 7),
        ([10, 1], 10)
    ]
)
class TestSolution:
    def test_minNumberOperations(self, target: List[int], output: int):
        sc = Solution()
        assert sc.minNumberOperations(target) == output