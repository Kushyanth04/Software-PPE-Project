import pytest
from typing import List
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/easy_2194_cells_in_a_range_on_an_excel_sheet')
from easy_2194_cells_in_a_range_on_an_excel_sheet_solution import Solution 

@pytest.mark.parametrize(
    "s, output",
    [
        ("K1:L2", ["K1", "K2", "L1", "L2"]),
        ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
        ("Z1:Z1", ["Z1"]),
        ("C3:D4", ["C3", "C4", "D3", "D4"]),
        ("G5:G5", ["G5"]),
        ("B2:B3", ["B2", "B3"]),
        ("M1:N2", ["M1", "M2", "N1", "N2"])
    ]
)
class TestSolution:
    def test_cellsInRange(self, s: str, output: List[str]):
        sol = Solution()
        assert sol.cellsInRange(s) == output