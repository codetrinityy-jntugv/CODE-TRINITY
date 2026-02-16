# Team Name: Code Trinity

def count_inventory(fruit_list: list[str]) -> dict[str, int]:
    """
    Create a frequency dictionary from a list of fruits.

    Args:
        fruit_list: A list of strings.

    Returns:
        A dictionary with fruit names as keys and counts as values.
    """
    if not isinstance(fruit_list, list):
        raise ValueError("fruit_list must be a list of strings.")

    inventory = {}

    for fruit in fruit_list:
        if not isinstance(fruit, str):
            raise ValueError("All elements in fruit_list must be strings.")

        if fruit in inventory:
            inventory[fruit] += 1
        else:
            inventory[fruit] = 1

    return inventory
