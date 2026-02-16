# Team Name: Code Trinity
def sanitize_email(raw_input: str) -> str:
    """
    Clean an email string and validate basic structure.

    Args:
        raw_input: A string containing a potential email address.

    Returns:
        The cleaned lowercase email or "Invalid Email".
    """
    if not isinstance(raw_input, str):
        raise ValueError("raw_input must be a string.")

    cleaned = raw_input.strip()
    cleaned = cleaned.lower()
    if not cleaned:
        return "Invalid Email"

    if cleaned.count("@") != 1:
        return "Invalid Email"

    return cleaned
