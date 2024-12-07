import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_2194_cells_in_a_range_on_an_excel_sheet')
from easy_2194_cells_in_a_range_on_an_excel_sheet_solution import Solution 


class TestSolution:
    @pytest.mark.parametrize("s, expected", [
        ("K1:L2", ["K1", "K2", "L1", "L2"]),
        ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
        ("Z1:Z1", ["Z1"]),
        ("C3:C5", ["C3", "C4", "C5"]),
        ("G2:H3", ["G2", "G3", "H2", "H3"]),
        ("A1:B2", ["A1", "A2", "B1", "B2"]),
        ("M5:M5", ["M5"]),
        ("X1:X3", ["X1", "X2", "X3"]),
        ("B2:B2", ["B2"]),
        ("Y3:Y3", ["Y3"])
    ])
    def test_cellsInRange(self, s: str, expected: List[str]):
        sol = Solution()
        assert sol.cellsInRange(s) == expected