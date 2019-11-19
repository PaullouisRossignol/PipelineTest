import pytest
from calculator import *

def test_add_neg():
    assert add(3, -12) == -9
def test_mul_decimals():
    assert mul(0.5, 24) == 12
def test_subs_neg():
    assert subs(20, -64) == -44
def test_add_nothing():
    assert add() == 0
def test_divide0():
    with pytest.raises(ZeroDivisionError):
        div(18, 5, 0)

