import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1312_minimum_insertion_steps_to_make_a_string_palindrome')  
from hard_1312_minimum_insertion_steps_to_make_a_string_palindrome_solution import Solution  


@pytest.mark.parametrize(
    "s, expected",
    [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
        ("g", 0),
        ("gg", 0),
        ("abc", 2),
        ("abcba", 0),
        ("abcd", 3),
        ("", 0),  # Edge case: empty string should require 0 insertions
        ("a" * 500, 0),  # Edge case: max length palindrome
        ("a" * 249 + "b" + "a" * 249, 1),  # Edge case: almost palindrome, large size
    ],
)
class TestSolution:
    def test_minInsertions(self, s: str, expected: int):
        sol = Solution()
        assert sol.minInsertions(s) == expected