"""
Challenge: Implement a Basic Calculator

Easy

In this challenge, you are required to write a function that takes two numbers 
and an operator as input and performs the specified operation on the input numbers. 
The calculator should be able to perform addition, subtraction, multiplication, 
and division.

Task:
-----------
Write a function calculate(number_1, number_2, operator) that takes two numbers 
and an operator as input and returns the result of the specified operation.

Supported operators: +, -, *, /

Example:
-----------
Input:  number_1 = 10, number_2 = 5, operator = "+"
Output: 15

Input:  number_1 = 12, number_2 = 4, operator = "/"
Output: 3.0
"""

def calculate(number_1: float, number_2: float, operator: str) -> float:
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "/":
        if number_2 != 0:
            return number_1 / number_2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unsupported operator"


# Example runs
if __name__ == "__main__":
    print(calculate(10, 5, "+"))  # Expected: 15
    print(calculate(10, 5, "-"))  # Expected: 5
    print(calculate(10, 5, "*"))  # Expected: 50
    print(calculate(10, 5, "/"))  # Expected: 2.0
    print(calculate(10, 0, "/"))  # Expected: Error: Division by zero
