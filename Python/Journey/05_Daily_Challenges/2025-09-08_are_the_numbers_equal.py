"""
Daily Challenge - 8th September 2025
-----------------------------------
Are the Numbers Equal?

Challenge:
Write a function named is_same_num that gets two numbers 
and returns True if the numbers are equal, and False if they are not equal.

Examples:
- is_same_num(4, 8) -> False
- is_same_num(2, 2) -> True
"""

def is_same_num(a, b):
    return a == b


# --- Example test calls (you can remove these when submitting) ---
if __name__ == "__main__":
    print(is_same_num(4, 8))  # Expected: False
    print(is_same_num(2, 2))  # Expected: True
