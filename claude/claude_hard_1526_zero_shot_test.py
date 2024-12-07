import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1526_minimum_number_of_increments_on_subarrays_to_form_a_target_array')  
from hard_1526_minimum_number_of_increments_on_subarrays_to_form_a_target_array_solution import Solution  

@pytest.mark.parametrize(
    "target, expected",
    [
        ([1, 2, 3, 2, 1], 3),
        ([3, 1, 1, 2], 4),
        ([3, 1, 5, 4, 2], 7),
        ([1] * 10, 1),
        ([100000] * 10, 100000),
    ],
)
def test_minNumberOperations(target: List[int], expected: int):
    sol = Solution()
    assert sol.minNumberOperations(target) == expected
