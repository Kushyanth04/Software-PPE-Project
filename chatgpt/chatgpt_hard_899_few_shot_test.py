import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_899_orderly_queue')
from hard_899_orderly_queue_solution import Solution 


@pytest.mark.parametrize(
    "s, k, output",
    [
        ("cba", 1, "acb"),
        ("baaca", 3, "aaabc"),
        ("abc", 1, "abc"),
        ("abc", 2, "abc"),
        ("abc", 3, "abc"),
        ("zxy", 2, "xyz"),
        ("zxy", 1, "xyz"),
        ("a", 1, "a"),
        ("abcdef", 6, "abcdef"),
        ("fedcba", 6, "abcdef"),
    ],
)
class TestSolution:
    def test_orderlyQueue(self, s: str, k: int, output: str):
        sol = Solution()
        assert sol.orderlyQueue(s, k) == output