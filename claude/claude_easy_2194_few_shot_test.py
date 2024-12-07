import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_2194_cells_in_a_range_on_an_excel_sheet')
from easy_2194_cells_in_a_range_on_an_excel_sheet_solution import Solution 

@pytest.mark.parametrize(
    "s, expected_output",
    [
        ("K1:L2", ["K1", "K2", "L1", "L2"]),
        ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
        ("A1:A1", ["A1"]),
        ("Z9:Z9", ["Z9"]),
    ],
)
class TestSolution:
    def test_cellsInRange(self, s: str, expected_output: List[str]):
        sc = Solution()
        assert sc.cellsInRange(s) == expected_output

    def test_empty_input(self):
        sc = Solution()
        with pytest.raises(ValueError):
            sc.cellsInRange("")

    def test_invalid_input_length(self):
        sc = Solution()
        with pytest.raises(ValueError):
            sc.cellsInRange("A1:B2:C3")

    def test_invalid_input_characters(self):
        sc = Solution()
        with pytest.raises(ValueError):
            sc.cellsInRange("A1:B@")

    def test_invalid_input_order(self):
        sc = Solution()
        with pytest.raises(ValueError):
            sc.cellsInRange("B2:A1")
