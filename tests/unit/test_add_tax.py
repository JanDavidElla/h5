import pytest
from src.pricing import add_tax

def test_add_tax_default_rate():
    assert add_tax(100.0) == pytest.approx(107.0)

def test_add_tax_custom_rate():
    assert add_tax(200.0, rate=0.10) == pytest.approx(220.0)

@pytest.mark.parametrize("rate", [-0.0001, -1.0])
def test_add_tax_negative_rate(rate):
    with pytest.raises(ValueError):
        add_tax(100.0, rate=rate)