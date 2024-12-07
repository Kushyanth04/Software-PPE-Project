import pytest
import sys
sys.path.insert(0, 'C:/Users/kushy/Desktop/SE_PROJECT - Main/dataset_leetcode/dataset_20241126_193530/medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers')  
from medium_1689_partitioning_into_minimum_number_of_deci_binary_numbers_solution import Solution  

@pytest.mark.parametrize(
    "n, expected_output",
    [
        ("32", 3),
        ("82734", 8),
        ("27346209830709182346", 9),
        ("1", 1),
        ("11", 2),
        ("10101010101010101010", 10),
        ("99999999999999999999", 20),
    ],
)
class TestSolution:
    def test_minPartitions(self, n: str, expected_output: int):
        sc = Solution()
        assert sc.minPartitions(n) == expected_output


@pytest.mark.parametrize(
    "n",
    [
        "",
        "0",
        "00000",
        "123456789",
        "9876543210",
    ],
)
def test_minPartitions_negative_cases(self, n: str):
    sc = Solution()
    with pytest.raises(Exception):
        sc.minPartitions(n)
