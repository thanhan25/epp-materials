from cobb_douglas import *
import pytest


def test_cobb_douglas():
    assert cobb_douglas(x1=1, x2=2, gamma1=1, gamma2=2, scale=1) == 4


def test_cobb_douglgas_scale():
    with pytest.raises(AssertionError) as excinfo:  
        cobb_douglas(x1=1, x2=2, gamma1=1, gamma2=2, scale=-1)
    assert str(excinfo.value) == "The parameter *scale* must be > 0."


def test_cobb_douglgas_x1():
    with pytest.raises(AssertionError) as excinfo:  
        cobb_douglas(x1=-2, x2=2, gamma1=1, gamma2=2, scale=2)
    assert str(excinfo.value) == "x1 must be non-negative."


def test_cobb_douglgas_x2():
    with pytest.raises(AssertionError) as excinfo:  
        cobb_douglas(x1=2, x2=-2, gamma1=1, gamma2=2, scale=2)
    assert str(excinfo.value) == "x2 must be non-negative."
