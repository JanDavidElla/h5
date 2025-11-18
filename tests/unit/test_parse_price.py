import pytest 
from src.pricing import parse_price

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("$1,234.50", 1234.50),
        ("12.5", 12.50),
        ("$0.99", 0.99)

    ]
) 

def test_parse_price_valid(raw, expected):
    assert parse_price(raw) == expected

@pytest.mark.parametrize("raw", ["", "abc"])
def test_parse_price_invalid_basic(raw):
    with pytest.raises(ValueError):
        parse_price(raw)