# Input Mastery in Python

# Challenge:
# Create a program that receives the user's name and age,
# then calculates and prints how old they will be in 10 years.
#
# Requirements:
# - Use input() to get the user's name and age
# - Store the inputs in variables
# - Convert the age to an integer and add 10
# - Print the result using an f-string in the format:
#   "In 10 years, [name] will be [age] years old."

# Get user's name
name = input()

# Get user's age as string and convert to integer
age = int(input())

# Calculate age in 10 years
age_in_10_years = age + 10

# Print the result
print(f"In 10 years, {name} will be {age_in_10_years} years old.")
