import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_771_jewels_and_stones')
import pytest
from easy_771_jewels_and_stones_solution import Solution


@pytest.mark.parametrize(
    "jewels, stones, output",
    [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("ABC", "ABCabc", 3),
        ("x", "xx", 2),
        ("", "abc", 0),
        ("abc", "", 0),
    ],
)
class TestSolution:
    def test_numJewelsInStones(self, jewels: str, stones: str, output: int):
        sc = Solution()
        assert sc.numJewelsInStones(jewels, stones) == output


@pytest.mark.parametrize("jewels, stones, output", [("aA", "", 0), ("", "", 0)])
class TestEdgeCases:
    def test_numJewelsInStones(self, jewels: str, stones: str, output: int):
        sc = Solution()
        assert sc.numJewelsInStones(jewels, stones) == output
