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
            ([1, 1, 1, 1, 1, 1], [[0], [1], [2], [3], [4], [5]]),
            ([5, 5, 5, 5, 5], [[0, 1, 2, 3, 4]]),
            ([2, 2, 2, 2, 2, 2], [[0, 1], [2, 3], [4, 5]]),
            ([1, 2, 3, 4, 5, 6], [[0], [1, 6], [2, 3, 4], [5]]),
            ([], []),
            ([1] * 500, [[i] for i in range(500)]),
        ],
    )
    def test_groupThePeople(self, groupSizes: List[int], expected: List[List[int]]):
        solution = Solution()
        assert solution.groupThePeople(groupSizes) == expected