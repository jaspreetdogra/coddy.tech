def multiple_of(n):
    # Challenge
    # Easy
    #
    # Write a function multiple_of(int) that takes a non-negative integer and returns True 
    # if it is a multiple of 5 or 7, otherwise False.
    #
    # Parameters:
    # n (int): A non-negative integer to check.
    #
    # Returns:
    # bool: True if n is a multiple of 5 or 7, otherwise False.
    #
    # Example:
    # Input: 10
    # Output: True  (because 10 is a multiple of 5)
    #
    # Input: 14
    # Output: True  (because 14 is a multiple of 7)
    #
    # Input: 8
    # Output: False (because 8 is not a multiple of 5 or 7)
    #
    # Edge Cases:
    # - Input = 0 → True (since 0 is technically a multiple of all integers)
    # - Negative inputs are not expected, but the logic would still hold mathematically.

    # Step 1: Check if n is divisible by either 5 or 7 using the modulo operator.
    # Step 2: Return True if any condition holds, else return False.
    return n % 5 == 0 or n % 7 == 0
