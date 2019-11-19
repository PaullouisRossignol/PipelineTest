import pytest
from calculator import *

def test_add_neg():
    assert add(-12, -64) == -76
def test_mul_decimals():
    assert mul(1.5, 24) == 36
def test_subs_neg():
    assert subs(-12, -64) == 76
def test_add_nothing():
    assert add() == 1
def test_divide0():
    with pytest.raises(ZeroDivisionError):
        div(5, 4, 0)

