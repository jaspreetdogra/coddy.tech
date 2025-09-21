"""
Challenge: How Much is True?

Create a function named `count_true` that calculates the number of True values in a list.
- The function should return 0 if the list is empty.
- All items in the list are boolean values.

Examples:
count_true([True, False, False, True, False]) ➞ 2
count_true([False, False, False, False]) ➞ 0
count_true([]) ➞ 0
"""

def count_true(values):
    """
    Counts the number of True values in a list of booleans.

    Parameters:
        values (list): A list containing boolean values (True or False).

    Returns:
        int: The number of True values in the list.
             If the list is empty, returns 0.
    """
    # If the list is empty, return 0
    if not values:
        return 0

    # Use the built-in list method `count()` to count how many True values are present
    return values.count(True)


# -----------------------------
# Example Test Cases
# -----------------------------

print(count_true([True, False, False, True, False]))  # Expected output: 2
print(count_true([False, False, False, False]))       # Expected output: 0
print(count_true([]))                                 # Expected output: 0
