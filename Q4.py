# Team Name: Code trinity

def get_ticket_price(age: int, is_student: bool) -> int:
    """
    Determine ticket price based on age and student status.

    Args:
        age: Integer representing the person's age.
        is_student: Boolean indicating if the person is a student.

    Returns:
        The ticket price as an integer.
    """
    if not isinstance(age, int):
        raise ValueError("age must be an integer.")
    if not (0 <= age <= 120):
        raise ValueError("age must be between 0 and 120 inclusive.")
    
    if not isinstance(is_student, bool):
        raise ValueError("is_student must be a boolean.")
 # Pricing rules
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:  # Ages 12 to 64
        if is_student:
            return 12
        else:
            return 15

