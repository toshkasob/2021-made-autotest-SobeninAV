import pytest


def test_equal():
    assert 5 = 5

def test_notequal():
    assert 3 != 5

def test_less():
    assert 3 < 5

def test_greater():
    assert 5 > 3

@pytest.mark.parametrize("inNumb", [-1000, -1, 0, 1, 1000 ])
def test_eval(inNumb):
    assert inNumb * 0 == 0
