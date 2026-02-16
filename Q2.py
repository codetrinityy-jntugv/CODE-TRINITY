# Team Name: code trinity 

def convert_seconds(total_seconds: int) -> str:
    """
    Convert total seconds into minutes and remaining seconds.

    Args:
        total_seconds: An integer representing time in seconds.

    Returns:
        A string formatted as "Xm Ys".
    """
    try:
        total_seconds = int(total_seconds)
    except (TypeError, ValueError):
        raise ValueError("total_seconds must be an integer.")
    if not (0 <= total_seconds <= 86400):
        raise ValueError("total_seconds must be between 0 and 86400 inclusive.")
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}m {seconds}s"
