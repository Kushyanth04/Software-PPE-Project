import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_1221_split_a_string_in_balanced_strings')
import pytest
from easy_1221_split_a_string_in_balanced_strings_solution import Solution
print(Solution) 
class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        ("RLRRLLRLRL", 4),
        ("RLRRRLLRLL", 2),
        ("LLLLRRRR", 1),
        ("RLLRRLRLRL", 4),
        ("RRLL", 1),
        ("LRLRLR", 3),
        ("RRRLLL", 1),
        ("RL" * 500, 500)  # Large balanced string
    ])
    def test_balancedStringSplit(self, s: str, expected: int):
        sol = Solution()
        assert sol.balancedStringSplit(s) == expected