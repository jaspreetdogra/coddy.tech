"""
Daily Challenge - 4th September 2025
------------------------------------
Adding Numbers in a String

Description:
This program takes a string of numbers separated by a comma and a space,
and outputs their sum. The program should handle negative numbers and
assume the input format is consistent.

Example:
Input:
"10, -5, 20"

Output:
25

Learning Goals:
- String splitting
- Type casting with int()
- Using sum() with lists
"""

def add_numbers_from_string(num_string):
    """
    Adds numbers from a comma-separated string.

    Parameters:
        num_string (str): A string containing numbers separated by ", ".
                          Example: "10, -5, 20"
    
    Returns:
        int: The sum of the numbers.
    """
    numbers = [int(n) for n in num_string.split(", ")]
    return sum(numbers)


# Example usage (main execution)
if __name__ == "__main__":
    num_string = input()  # e.g., "10, -5, 20"
    result = add_numbers_from_string(num_string)
    print(result)
