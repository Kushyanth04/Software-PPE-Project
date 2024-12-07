import pytest
from easy_771_jewels_and_stones_solution import Solution


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
