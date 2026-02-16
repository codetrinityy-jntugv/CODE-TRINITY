# Team Name: code trinity

def calculate_total_bill(amount: float, tip_percent: int) -> float:
    """
    Calculate the total bill including tip.

    Args:
        amount: The initial bill amount (numeric)
        tip_percent: The tip percentage (integer)

    Returns:
        The total bill rounded to 2 decimal places.
    """
    amount = float(amount)
    tip_percent = float(tip_percent)
    if not (0 <= amount <= 10000):
        raise ValueError("amount must be between 0 and 10000 inclusive.")
    if not (0 <= tip_percent <= 100):
        raise ValueError("tip_percent must be between 0 and 100 inclusive.")
    total = amount + (amount * tip_percent / 100)
    return round(total, 2)


