import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1282_group_the_people_given_the_group_size_they_belong_to')  
from medium_1282_group_the_people_given_the_group_size_they_belong_to_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize(
        "groupSizes, expected_output",
        [
            ([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]]),
            ([2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]]),
            ([], []),
            ([1] * 500, [[i] for i in range(500)]),
            ([500], [[i for i in range(500)]]),
        ],
    )
    def test_groupThePeople(self, groupSizes: List[int], expected_output: List[List[int]]):
        sc = Solution()
        assert sc.groupThePeople(groupSizes) == expected_output

    def test_groupThePeople_negative(self):
        sc = Solution()
        with pytest.raises(Exception):
            sc.groupThePeople([0, 3, 2])