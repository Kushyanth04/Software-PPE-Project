import pytest
from hard_1312_minimum_insertion_steps_to_make_a_string_palindrome_solution import Solution


@pytest.mark.parametrize("s, output", [("zzazz", 0), ("mbadm", 2), ("leetcode", 5)])
class TestSolution:
    def test_minInsertions(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.minInsertions(
                s,
            )
            == output
        )
