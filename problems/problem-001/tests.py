# tests.py
import pytest
from solution import sum_of_two

def test_sum_of_two():
    assert sum_of_two(2, 3) == 5
    assert sum_of_two(-1, 1) == 0
    assert sum_of_two(-5, -5) == -10
    assert sum_of_two(0, 0) == 0