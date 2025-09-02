# Recap - Till 120
# Challenge: Beginner
# Task:
# Write a program that gets the user's age as input.
# The program will output (print) the number of missing years till 120 (in a specific format).
# For example, for input 25, the expected output is: "95 years till 120"
# Make sure to not print anything else!

# Read user's age as integer
age = int(input())

# Calculate remaining years till 120
till = 120 - age

# Print result in the required format
print(f"{till} years till 120")
