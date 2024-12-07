import pytest
from hard_899_orderly_queue_solution import Solution


@pytest.mark.parametrize("s, k, output", [("cba", 1, "acb"), ("baaca", 3, "aaabc")])
class TestSolution:
    def test_orderlyQueue(self, s: str, k: int, output: str):
        sc = Solution()
        assert (
            sc.orderlyQueue(
                s,
                k,
            )
            == output
        )
