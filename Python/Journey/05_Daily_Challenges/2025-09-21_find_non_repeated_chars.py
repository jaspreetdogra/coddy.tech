"""
Challenge: Find the First Non-Repeated Character

Write a function `first_non_repeated_char(s)` that takes a string as input
and returns the first non-repeated character. If there is no such character,
return an empty string.

Examples:
first_non_repeated_char("swiss") ➞ "w"
first_non_repeated_char("aabbcc") ➞ ""
"""

def first_non_repeated_char(s):
    """
    Finds the first non-repeated character in a string.

    Parameters:
        s (str): Input string

    Returns:
        str: The first character that does not repeat, or an empty string if none exists
    """
    # Dictionary to store the count of each character
    char_count = {}

    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate again to find the first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char

    # Return empty string if all characters are repeated
    return ""


# -----------------------------
# Example Test Cases
# -----------------------------
print(first_non_repeated_char("swiss"))   # Expected output: "w"
print(first_non_repeated_char("aabbcc"))  # Expected output: ""
print(first_non_repeated_char("hello"))   # Expected output: "h"
print(first_non_repeated_char(""))        # Expected output: ""
