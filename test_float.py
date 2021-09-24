import pytest
import math


def test_equal():
    assert 5.0 / 10.0 = 0.5

def test_notequal():
    assert 3.0 / 10.0 != 3.0

def test_less():
    assert 3.0 < 3.000001

def test_greater():
    assert 5.0 - 4.999999 > 0

@pytest.mark.parametrize("inNumb", [-1000.5, -1.1, 0.0, 1.1, 1000.5 ])
def test_multzero(inNumb):
    assert inNumb * 0 == 0

def test_error():
    try:
        assert 0.000001 / math.exp(1000)
    except FloatingPointError:
        pass
