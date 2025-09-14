"""
Square into Integer
-------------------

Challenge: Medium

Write a function `square_into_integer(n)` that takes an integer n and returns 
the count of integer squares from 1 to n.

Example:
    square_into_integer(10) -> 3
    (since 1^2 = 1, 2^2 = 4, 3^2 = 9 are <= 10)

Explanation:
-------------
We are counting how many perfect squares are less than or equal to n.
This can be calculated using `math.isqrt(n)` which gives the integer square root of n.
"""

import math 

def square_into_integer(n):
    """
    Count how many perfect squares are less than or equal to n.

    Args:
        n (int): The input integer

    Returns:
        int: Count of integer squares from 1 to n
    """
    return math.isqrt(n)


# Example test cases
if __name__ == "__main__":
    print(square_into_integer(10))  # Output: 3
    print(square_into_integer(25))  # Output: 5
    print(square_into_integer(1))   # Output: 1
    print(square_into_integer(50))  # Output: 7
