"""
min_max.py
Challenge: Easy
Return the minimum and maximum values from a list of integers.

Write a function min_max that takes a list of integers and returns a list
containing the minimum and maximum values, in that order.

Examples:
    min_max([2, 5, 1, 9, 3]) -> [1, 9]
    min_max([5, 18, 12, 1, 99, 100]) -> [1, 100]
"""

from typing import List

def min_max(numbers: List[int]) -> List[int]:
    """
    Return [min_value, max_value] for the given list of integers.

    Args:
        numbers: List[int] - list of integers (must be non-empty)

    Returns:
        List[int] - [minimum, maximum]

    Raises:
        ValueError: if numbers is empty
    """
    if not numbers:
        raise ValueError("min_max() requires a non-empty list of integers.")
    return [min(numbers), max(numbers)]


if __name__ == "__main__":
    # Example tests
    tests = [
        [2, 5, 1, 9, 3],
        [5, 18, 12, 1, 99, 100],
        [42],                       # single element
        [-5, 0, 5, 10, -10]         # negative numbers included
    ]

    for t in tests:
        print(min_max(t))
