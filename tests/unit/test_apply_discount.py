import pytest
from src.pricing import apply_discount

def test_apply_discount_zero_percent():
    assert apply_discount(100.0, 0) == pytest.approx(100.0)

def test_apply_discount_typical_percent():
    assert apply_discount(200.0, 10) == pytest.approx(180.0)

def test_apply_discount_negative():
    with pytest.raises(ValueError):
        apply_discount(50.0, -1)


#In case with large percentage
def test_apply_discount_large_percent():
    assert apply_discount(100.0, 150) == pytest.approx(-50.0)