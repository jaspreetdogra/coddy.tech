# Cast in Python

# To convert the input to a different type, we need to cast.
# For example, to cast a string to an int (a whole number), we can write:
#
# var = input()
# var = int(var)
#
# Or in one line:
# var = int(input())
#
# If the input is a number, e.g., 5, 4, 54 then var will hold a number.
# If the input contains an invalid number like 5ab, bb, akt, etc., the program will fail.

# Table of common type casts:
# int()   -> Convert to a whole number
# float() -> Convert to a real number
# bool()  -> Convert to a boolean
# str()   -> Convert to a string

# Important: Using the correct type affects the output.
# Adding two strings will concatenate them:
# "5" + "5" = "55"
# Adding two numbers will sum them:
# 5 + 5 = 10

# Quiz context:
# 1. What does int() do? -> Convert a value to a whole number
# 2. Which type conversion to obtain a real number from a string? -> float()

# Challenge: Beginner
# In this challenge, you'll work with multiple inputs and perform calculations.

# How to receive multiple inputs:
# var1 = input()  # First input
# var2 = input()  # Second input

# Task:
# - Read the first number from input and store it in a variable
# - Read the second number from input and store it in another variable
# - Convert both variables to float type (for decimal numbers)
# - Calculate the multiplication of these two numbers
# - Print the result
# Example: Inputs 2 and 4.5 -> Output: 9.0

# Read and convert inputs to float
var1 = float(input())
var2 = float(input())

# Multiply the two numbers
multi = var1 * var2

# Print the result
print(multi)
