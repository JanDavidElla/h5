from src.pricing import format_currency
import pytest

@pytest.mark.parametrize(
    "amount, expected",
    [
        (1234.5, "$1234.50"),
        (0, "$0.00"),
        (12.345, "#12.35"),
    ],
)

def test_format_currency(amount, expected):
    assert format_currency(amount) == expected
