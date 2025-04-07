"""
Template for Hard array test cases, using Build a Matrix With Conditions as example.
"""
import pytest
from q_1526_minimumNumberOfIncrementsOnSubarraysToFormATargetArray import Solution


@pytest.mark.parametrize(
    "target, output", [([1, 2, 3, 2, 1], 3), ([3, 1, 1, 2], 4), ([3, 1, 5, 4, 2], 7)]
)
class TestSolution:
    def test_minNumberOperations(self, target: List[int], output: int):
        sc = Solution()
        assert (
            sc.minNumberOperations(
                target,
            )
            == output
        )

"""
