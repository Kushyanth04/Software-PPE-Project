import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1282_group_the_people_given_the_group_size_they_belong_to')  
from medium_1282_group_the_people_given_the_group_size_they_belong_to_solution import Solution  

@pytest.mark.parametrize(
    "groupSizes, expected_output", [
        ([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]]),
        ([2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]]),
        ([1, 1, 1, 1], [[0], [1], [2], [3]]),
        ([2, 2, 2, 2], [[0, 1], [2, 3]]),
        ([5, 5, 5, 5, 5], [[0, 1, 2, 3, 4]]),
        ([1], [[0]]),
        ([1, 2, 2], [[0], [1, 2]])
    ]
)
class TestSolution:
    def test_groupThePeople(self, groupSizes: List[int], expected_output: List[List[int]]):
        sol = Solution()
        result = sol.groupThePeople(groupSizes)
        # Since multiple correct answers are possible, we need to validate the structure of the result
        assert len(result) == len(expected_output), "Number of groups should match the expected output"
        result_group_sizes = [len(group) for group in result]
        expected_group_sizes = [len(group) for group in expected_output]
        assert sorted(result_group_sizes) == sorted(expected_group_sizes), "Group sizes should match the expected sizes"
        # Check if every person is exactly in one group
        all_members = [member for group in result for member in group]
        assert sorted(all_members) == sorted(range(len(groupSizes))), "Every person should appear exactly once"
