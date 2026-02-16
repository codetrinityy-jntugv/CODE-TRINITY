# Team Name: Code Trinity
def generate_threes(start: int, end: int) -> list[int]:
    """
    Generate a list of numbers from start to end, skipping by 3.

    Args:
        start: The starting integer.
        end: The integer to stop before.

    Returns:
        A list of integers incremented by 3.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start and end must be integers.")

    if start >= end:
        return []
    return list(range(start, end, 3))
