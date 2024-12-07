import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1312_minimum_insertion_steps_to_make_a_string_palindrome')  
from hard_1312_minimum_insertion_steps_to_make_a_string_palindrome_solution import Solution  

class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
        ("a", 0),
        ("ab", 1),
        ("abc", 2),
        ("abcba", 0),
        ("abcd", 3),
        ("abcde", 4),
        ("race", 3),
        ("racecar", 0),
        ("", 0),
        ("aa", 0),
        ("aba", 0),
        ("abca", 1),
        ("abcda", 2),
        ("abcdca", 1),
        ("a" * 500, 0),  # Edge case: max length palindrome
        ("a" + "b" * 498 + "a", 498)  # Edge case: almost all characters need to be mirrored
    ])
    def test_minInsertions(self, s: str, expected: int):
        sol = Solution()
        assert sol.minInsertions(s) == expected