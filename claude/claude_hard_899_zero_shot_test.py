import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_899_orderly_queue')
from hard_899_orderly_queue_solution import Solution 

class TestSolution:
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("cba", 1, "acb"),
            ("baaca", 3, "aaabc"),
            ("a", 1, "a"),
            ("abcdefghijklmnopqrstuvwxyz", 26, "abcdefghijklmnopqrstuvwxyz"),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaa", 1, "aaaaaaaaaaaaaaaaaaaaaaaaaa"),
            ("zzzzzzzzzzzzzzzzzzzzzzzzz", 26, "azzzzzzzzzzzzzzzzzzzzzzzzz"),
        ],
    )
    def test_orderlyQueue(self, s: str, k: int, expected: str) -> None:
        solution = Solution()
        assert solution.orderlyQueue(s, k) == expected