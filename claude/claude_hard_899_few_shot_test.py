import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_899_orderly_queue')
from hard_899_orderly_queue_solution import Solution 


@pytest.mark.parametrize(
    "s, k, output",
    [
        ("cba", 1, "acb"),
        ("baaca", 3, "aaabc"),
        ("abc", 2, "abc"),
        ("a", 1, "a"),
        ("abcdefghijklmnopqrstuvwxyz", 26, "abcdefghijklmnopqrstuvwxyz"),
    ],
)
class TestSolution:
    def test_orderlyQueue(self, s: str, k: int, output: str):
        sc = Solution()
        assert sc.orderlyQueue(s, k) == output


@pytest.mark.parametrize(
    "s, k",
    [
        ("", 0),
        ("abcdefghijklmnopqrstuvwxyz", 0),
        ("abcdefghijklmnopqrstuvwxyz", 27),
    ],
)
def test_invalid_inputs(s: str, k: int):
    sc = Solution()
    with pytest.raises(Exception):
        sc.orderlyQueue(s, k)