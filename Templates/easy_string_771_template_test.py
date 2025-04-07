"""
Template for Easy string test cases, using Split a String in Balanced Strings as example.
"""
import pytest
from q_0771_jewelsAndStones import Solution


@pytest.mark.parametrize(
    "jewels, stones, output", [("aA", "aAAbbbb", 3), ("z", "ZZ", 0)]
)
class TestSolution:
    def test_numJewelsInStones(self, jewels: str, stones: str, output: int):
        sc = Solution()
        assert (
            sc.numJewelsInStones(
                jewels,
                stones,
            )
            == output
        )

"""
