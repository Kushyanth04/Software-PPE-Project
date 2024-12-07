import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1221_split_a_string_in_balanced_strings')
import pytest
from easy_1221_split_a_string_in_balanced_strings_solution import Solution

@pytest.mark.parametrize(
    "s, output",
    [
        ("RLRRLLRLRL", 4),
        ("RLRRRLLRLL", 2),
        ("LLLLRRRR", 1),
        ("RLLLLRRRLR", 3),
        ("RLRLRLRLRLRL", 3),
        ("RRRRRRRRRRR", 1),
        ("LLLLLLLLLL", 1),
        ("", 0),
    ],
)
class TestSolution:
    def test_balancedStringSplit(self, s: str, output: int):
        sc = Solution()
        assert sc.balancedStringSplit(s) == output