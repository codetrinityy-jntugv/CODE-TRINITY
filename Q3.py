# Team Name: Code trinity 

def average_passing_grades(grades: list[int]) -> float:
    """
    Calculate the average of grades that are 50 or higher.

    Args:
        grades: A list of integers representing scores.

    Returns:
        The average of passing grades as a float, or 0.0 if none exist.
    """
    if not isinstance(grades, list):
        raise ValueError("grades must be a list of integers.")

    total = 0
    count = 0

    for grade in grades:
        if not isinstance(grade, int):
            raise ValueError("All grades must be integers.")
        if not (0 <= grade <= 100):
            raise ValueError("Each grade must be between 0 and 100 inclusive.")
        if grade >= 50:
            total += grade
            count += 1

    if count == 0:
        return 0.0

    return float(total / count)

