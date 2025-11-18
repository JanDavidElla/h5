from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency

def test_order_integration(tmp_path):
    csv_path = tmp_path / "order.csv"
    csv_path.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    items = load_order(csv_path)
    prices = [price for _, price in items]

    total = bulk_total(prices, discount_percent=10, tax_rate=0.07)

    out_path = tmp_path / "receipt.txt"
    write_receipt(out_path, items, discount_percent=10, tax_rates=0.07)

    text=out_path.read_text(encoding="utf-8")
    assert "widget: $10.00" in text
    assert "gizmo: $5.50" in text
    assert "TOTAL: " in text