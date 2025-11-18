import pytest 
from src.pricing import bulk_total

def test_bulk_total_simple_list():
    prices = [10.00, 5.50]
    discounted = 15.50 * 0.90
    total_with_tax = discounted * 1.1
    assert bulk_total(prices, discount_percent=10, tax_rate=0.10) == pytest.approx(15.345, rel=1e-9)
