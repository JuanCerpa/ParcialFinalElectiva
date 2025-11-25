import pytest
from src.calculos import suma, division

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(10, 0)