# Team Name: Code Trinity 

def convert_temperature(value: float, unit: str) -> float | str:
    """
    Convert temperature between Celsius and Fahrenheit.

    Args:
        value: The temperature value to convert.
        unit: The unit of the input value ('C' for Celsius, 'F' for Fahrenheit)

    Returns:
        The converted temperature as a float (rounded to 1 decimal),
        or "Invalid Unit" if the unit is unknown.
    """

    # Bug Fix 1:
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise ValueError("value must be numeric.")

    # Bug Fix 2:
    if not isinstance(unit, str) or len(unit) != 1:
        return "Invalid Unit"

    # Bug Fix 3:
    unit = unit.upper()

    # Bug Fix 4:
    if unit == 'C':
        result = (value * 9 / 5) + 32
        return round(result, 1)

    # Bug Fix 5:
    elif unit == 'F':
        result = (value - 32) * 5 / 9
        return round(result, 1)

    # Bug Fix 6:
    else:
        return "Invalid Unit"




