"""
Simple Interest Calculator
--------------------------

This program calculates Simple Interest using the formula:

    Simple Interest = Principal × Rate × Time

Where:
- Principal (p): The initial amount of money
- Rate (r): The annual interest rate in decimal form (e.g., 0.05 for 5%)
- Time (t): The duration of the loan in years

Function:
    calculate_simple_interest(p, r, t)

Arguments:
    p (int or float): Principal amount
    r (float): Annual interest rate (in decimal form)
    t (int or float): Loan duration in years

Returns:
    int: The calculated simple interest amount (converted to integer)

Example Usage:
    >>> calculate_simple_interest(1000, 0.05, 2)
    100
"""

def calculate_simple_interest(p, r, t):
    """
    Calculate simple interest on a loan.

    Args:
        p (int or float): Principal amount
        r (float): Annual interest rate in decimal form (e.g., 0.05 for 5%)
        t (int or float): Loan duration in years

    Returns:
        int: Simple interest amount
    """
    interest = p * r * t
    return int(interest)


# Example test runs
if __name__ == "__main__":
    print("Simple Interest Calculator Examples:")
    print(calculate_simple_interest(1000, 0.05, 2))   # Expected: 100
    print(calculate_simple_interest(5000, 0.1, 1))    # Expected: 500
    print(calculate_simple_interest(1200, 0.07, 3))   # Expected: 252
