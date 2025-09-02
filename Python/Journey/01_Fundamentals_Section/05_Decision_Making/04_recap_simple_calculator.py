"""
Recap - Simple Calculator

Theory:

We can use if-elif-else statements to perform different actions based on conditions.

Example:
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
else:
    result = 0

In this challenge, the operator can be '+', '-', '*', or '/'.
"""

# Challenge - Beginner
# You are given a code which gets as input two numbers n1 and n2 and a character op.
# The possible values for op are '+', '-', '/', and '*'.
# Your task is to set the variable 'result' based on the operator.

n1 = int(input("Enter first number: "))  # Don't change this line
n2 = int(input("Enter second number: "))  # Don't change this line
op = input("Enter operator (+, -, *, /): ")  # Don't change this line
result = 0

# Solution
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    result = n1 / n2
elif op == '*':
    result = n1 * n2
else:
    print("Wrong Input!")

# Don't change the line below
print(f"result = {result}")
