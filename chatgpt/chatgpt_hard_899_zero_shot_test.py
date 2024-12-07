import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_899_orderly_queue')
from hard_899_orderly_queue_solution import Solution 

class TestSolution:
    @pytest.mark.parametrize("s, k, expected", [
        ("cba", 1, "acb"),
        ("baaca", 3, "aaabc"),
        ("abc", 1, "abc"),
        ("abc", 3, "abc"),
        ("zxy", 2, "xyz"),
        ("a", 1, "a"),
        ("abcdef", 1, "abcdef"),
        ("abcdef", 6, "abcdef"),
        ("zyxwvutsrqponmlkjihgfedcba", 1, "abcdefghijklmnopqrstuvwxyz"),
        ("zyxwvutsrqponmlkjihgfedcba", 25, "abcdefghijklmnopqrstuvwxyz"),
    ])
    def test_orderlyQueue(self, s: str, k: int, expected: str):
        sol = Solution()
        result = sol.orderlyQueue(s, k)
        assert result == expected