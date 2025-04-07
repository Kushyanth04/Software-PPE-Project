"""
Template for Easy string test cases, using Jewels and Stones as example.
"""
import pytest
from q_1221_splitAStringInBalancedStrings import Solution


@pytest.mark.parametrize(
    "s, output", [("RLRRLLRLRL", 4), ("RLRRRLLRLL", 2), ("LLLLRRRR", 1)]
)
class TestSolution:
    def test_balancedStringSplit(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.balancedStringSplit(
                s,
            )
            == output
        )

"""
