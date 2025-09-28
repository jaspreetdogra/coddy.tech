"""
Daily Challenge: Check if a String Contains Only Unique Characters

Difficulty: Easy

Guidelines:
1. Write a function named `has_unique_chars` that takes a non-empty string `s`.
2. The function should return True if all characters in the string are unique.
3. If any character repeats, return False.
4. Avoid using nested loops for efficiency.
5. Hint: Use a Python set to check uniqueness quickly.

Example:
    has_unique_chars("hello")   -> False
    has_unique_chars("world")   -> True
"""

def has_unique_chars(s):
    """
    Check if a string contains only unique characters.

    Args:
        s (str): Non-empty input string

    Returns:
        bool: True if all characters are unique, False otherwise
    """
    # Convert string to a set to remove duplicates
    # Compare the length of the set with the original string
    return len(s) == len(set(s))

