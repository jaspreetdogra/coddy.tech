# Input in Python

# Theory:
# Programs usually receive values from an outer source, like a user.
# To get input from a user, we use input():
# Example:
# var = input()
# Note: Input is always stored as a string. So if the user enters 56, var holds "56"

# Quiz:
# 1) How do you store the user's input in a variable named userAge?
#    Correct answer: userAge = input()
#
# 2) If a user inputs 42, which representation is correct for the variable storing this input?
#    Correct answer: "42"

# Challenge:
# Write a program that gets input from the user (their name), 
# and outputs "Hello, <name>"

user = input()  # Get user's name
print(f"Hello, {user}")  # Output greeting with user's name
