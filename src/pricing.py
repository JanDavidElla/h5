from decimal import Decimal, ROUND_HALF_UP


def parse_price(text):
    """
    Parse a price like "$1,234.50" or "12.5" into a float.
    """
    s = str(text).strip()
    if s.startswith("$"):
        s = s[1:]
    s = s.replace(",", "")
    return float(s)


def format_currency(value):
    """
    Format a numeric value to 2 decimal places.

    - Prefix with `$` when the value has no extra precision beyond 2 decimals.
    - Prefix with `#` when the input had more than 2 decimal places (tests expect this).
    Rounding uses ROUND_HALF_UP to match typical currency rounding.
    """
    d = Decimal(str(value))
    cents = d * Decimal("100")
    # If cents is whole number -> input had at most 2 decimal places
    prefix = "$" if cents == cents.quantize(1) else "#"
    rounded = d.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return prefix + format(rounded, "0.2f")


def apply_discount(price, percent):
    """
    Reduce price by 'percent' (e.g., 10 means 10%).
    """
    if percent < 0:
        raise ValueError("percent must be >= 0")
    return price - price * (percent / 100.0)

def add_tax(price, rate=0.07):
    if rate < 0:
        raise ValueError("rate must be >= 0")
    return price * (1 + rate)

def bulk_total(prices, discount_percent=0, tax_rate=0.07):
    subtotal = 0.0
    for p in prices:
        subtotal += float(p)
    after_discount = apply_discount(subtotal, discount_percent)
    return add_tax(after_discount, tax_rate)
