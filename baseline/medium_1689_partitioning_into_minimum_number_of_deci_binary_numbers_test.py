import pytest
from medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers_solution import Solution


@pytest.mark.parametrize(
    "n, output", [("32", 3), ("82734", 8), ("27346209830709182346", 9)]
)
class TestSolution:
    def test_minPartitions(self, n: str, output: int):
        sc = Solution()
        assert (
            sc.minPartitions(
                n,
            )
            == output
        )
