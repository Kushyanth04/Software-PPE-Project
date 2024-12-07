import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/hard_1312_minimum_insertion_steps_to_make_a_string_palindrome')  
from hard_1312_minimum_insertion_steps_to_make_a_string_palindrome_solution import Solution  

@pytest.mark.parametrize(
    "s, output",
    [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
        ("a", 0),
        ("ab", 1),
        ("aaa", 0),
        ("abcba", 0),
        ("abcde", 4),
        ("" * 500 + "a", 499),
    ],
)
class TestSolution:
    def test_minInsertions(self, s: str, output: int):
        sc = Solution()
        assert sc.minInsertions(s) == output

    def test_minInsertions_empty_string(self):
        sc = Solution()
        assert sc.minInsertions("") == 0

    def test_minInsertions_invalid_input(self):
        sc = Solution()
        with pytest.raises(TypeError):
            sc.minInsertions(123)
