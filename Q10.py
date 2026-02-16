# Team Name: Code Trinity
def organize_scores(scores: list[int], descending: bool) -> list[int]:
    """
    Sort scores without modifying the original list.

    Args:
        scores: A list of integers.
        descending: Boolean indicating sort order.

    Returns:
        A new sorted list of integers.
    """
    if not isinstance(scores, list):
        raise ValueError("scores must be a list of integers.")
    if not isinstance(descending, bool):
        raise ValueError("descending must be a boolean.")

    for score in scores:
        if not isinstance(score, int):
            raise ValueError("All elements in scores must be integers.")
 # Used sorted() to avoid modifying original list
    return sorted(scores, reverse=descending)
