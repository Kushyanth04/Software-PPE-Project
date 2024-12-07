import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2785_sort_vowels_in_a_string')  
from medium_2785_sort_vowels_in_a_string_solution import Solution 

@pytest.mark.parametrize(
    "s, output",
    [
        ("lEetcOde", "lEOtcede"),  
        ("aEbcdiOu", "aEbciOu"),  
        ("rhythms", "rhythms"), 
        ("AaEeIiOoUu", "AEIOUaeiou"),  
        ("", ""), 
    ],
)
class TestSolution:
    def test_sortVowels(self, s: str, output: str):
        sc = Solution()
        assert sc.sortVowels(s) == output