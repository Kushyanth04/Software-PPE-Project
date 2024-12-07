import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_2785_sort_vowels_in_a_string')  
from medium_2785_sort_vowels_in_a_string_solution import Solution 

class TestSolution:
    @pytest.mark.parametrize("s, output", [
        ("lEetcOde", "lEOtcede"),  # Mixed vowels and consonants
        ("lYmpH", "lYmpH"),  # No vowels
        ("aeiou", "aeiou"),  # All vowels, already sorted
        ("uoiea", "aeiou"),  # All vowels, reverse sorted
        ("", ""),  # Empty string
        ("b", "b"),  # Single consonant
    ])
    def test_sortVowels(self, s: str, output: str):
        solution = Solution()
        assert solution.sortVowels(s) == output