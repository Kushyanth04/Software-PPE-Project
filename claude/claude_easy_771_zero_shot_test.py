import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_771_jewels_and_stones')
import pytest
from easy_771_jewels_and_stones_solution import Solution

class TestSolution:
    @pytest.mark.parametrize(
        "jewels, stones, expected",
        [
            ("aA", "aAAbbbb", 3),
            ("z", "ZZ", 0),
            ("ABC", "ABCabc", 3),
            ("", "abc", 0),
            ("abc", "", 0),
        ],
    )
    def test_numJewelsInStones(self, jewels: str, stones: str, expected: int):
        sol = Solution()
        assert sol.numJewelsInStones(jewels, stones) == expected

    @pytest.mark.parametrize(
        "jewels, stones, expected",
        [
            ("aA", "", 0),
            ("", "", 0),
            ("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", 0),
            ("a" * 50, "b" * 50, 0),
            ("a" * 50 + "b", "a" * 50, 50),
        ],
    )
    def test_numJewelsInStones_edge_cases(self, jewels: str, stones: str, expected: int):
        sol = Solution()
        assert sol.numJewelsInStones(jewels, stones) == expected