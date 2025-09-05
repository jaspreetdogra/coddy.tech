"""
Daily Challenge - 5th September 2025
------------------------------------
Calculate the Sum of Digits in a Number

Description:
Write a function sum_of_digits(num) that takes a non-negative integer
as input and returns the sum of its digits.

Example:
Input:
123

Output:
6

Explanation:
1 + 2 + 3 = 6

Learning Goals:
- While loop usage
- Modulus (%) to extract digits
- Integer division (//) to reduce the number
"""

def sum_of_digits(num):
    """
    Calculates the sum of digits in a given non-negative integer.

    Parameters:
        num (int): Non-negative integer
    
    Returns:
        int: Sum of digits
    """
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


# Example usage (main execution)
if __name__ == "__main__":
    try:
        n = int(input())  # e.g., 123
        print(sum_of_digits(n))
    except EOFError:
        # No input provided — safely exit without printing
        pass
