import pytest

@pytest.fixture
def sample_data():
    return [("widget", 10.00), ("gizmo", 5.50), ("clip", 7.99)]

@pytest.fixture
def sample_prices(sample_data):
    return [price for _, price in sample_data]