"""
Revolutionary Calculator
========================

Challenge:
Create a function named calculate that takes an arithmetic expression as input and returns the result. 
The input will be a non-empty string containing only +, -, and non-negative integers. 
The function should handle an unlimited number of operands and operators. 
Do NOT use the built-in eval function.

Example Usage:
---------------
calculate("2+3-1")        -> 4
calculate("10+20+30-15")  -> 45
calculate("100-50+25-10") -> 65

"""

def calculate(expression):
    """
    Evaluate a simple arithmetic expression containing only +, - and non-negative integers.

    Args:
        expression (str): The arithmetic expression as a string.

    Returns:
        int: The result of the expression.
    """
    num = 0
    result = 0
    sign = 1  # 1 for addition, -1 for subtraction

    # Append a '+' at the end to handle the last number
    for ch in expression + '+':
        if ch.isdigit():
            num = num * 10 + int(ch)  # build multi-digit numbers
        elif ch in '+-':
            result += sign * num
            num = 0
            sign = 1 if ch == '+' else -1

    return result


if __name__ == "__main__":
    # Test cases
    print(calculate("2+3-1"))          # Output: 4
    print(calculate("10+20+30-15"))    # Output: 45
    print(calculate("100-50+25-10"))   # Output: 65
    print(calculate("5+5+5+5-10-5"))   # Output: 5
