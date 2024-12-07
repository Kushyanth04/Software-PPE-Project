from typing import List
import pytest
from easy_2194_cells_in_a_range_on_an_excel_sheet_solution import Solution


@pytest.mark.parametrize(
    "s, output",
    [
        ("K1:L2", ["K1", "K2", "L1", "L2"]),
        ("A1:F1", ["A1", "B1", "C1", "D1", "E1", "F1"]),
    ],
)
class TestSolution:
    def test_cellsInRange(self, s: str, output: List[str]):
        sc = Solution()
        assert (
            sc.cellsInRange(
                s,
            )
            == output
        )
