import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1282_group_the_people_given_the_group_size_they_belong_to')  
from medium_1282_group_the_people_given_the_group_size_they_belong_to_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "groupSizes, expected",
        [
            ([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]]),
            ([2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]]),
            ([1, 1, 1, 1], [[0], [1], [2], [3]]),
            ([4, 4, 4, 4], [[0, 1, 2, 3]]),
            ([2, 2, 2, 2, 2, 2], [[0, 1], [2, 3], [4, 5]]),
            ([5, 5, 5, 5, 5, 1], [[5], [0, 1, 2, 3, 4]]),
            ([1], [[0]]),
            ([2, 2], [[0, 1]]),
            ([3, 3, 3, 3, 3, 3], [[0, 1, 2], [3, 4, 5]])
        ]
    )
    def test_groupThePeople(self, groupSizes: List[int], expected: List[List[int]]):
        sol = Solution()
        result = sol.groupThePeople(groupSizes)
        # Since multiple valid solutions are possible, we check if the result is valid
        assert len(result) == len(expected)
        # Check if each group is valid
        group_size_map = {i: size for i, size in enumerate(groupSizes)}
        for group in result:
            group_size = len(group)
            assert all(group_size_map[person] == group_size for person in group)