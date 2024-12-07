import pytest
from medium_2785_sort_vowels_in_a_string_solution import Solution


@pytest.mark.parametrize("s, output", [("lEetcOde", "lEOtcede"), ("lYmpH", "lYmpH")])
class TestSolution:
    def test_sortVowels(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.sortVowels(
                s,
            )
            == output
        )
