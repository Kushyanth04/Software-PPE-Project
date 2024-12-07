from typing import List
import pytest
from medium_1282_group_the_people_given_the_group_size_they_belong_to_solution import Solution


@pytest.mark.parametrize(
    "groupSizes, output",
    [
        ([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]]),
        ([2, 1, 3, 3, 3, 2], [[1], [0, 5], [2, 3, 4]]),
    ],
)
class TestSolution:
    def test_groupThePeople(self, groupSizes: List[int], output: List[List[int]]):
        sc = Solution()
        assert (
            sc.groupThePeople(
                groupSizes,
            )
            == output
        )
