"""
Nested If-Else

Theory:

Nested If-Else statements allow you to check multiple conditions by placing one if-else statement inside another.

Example:

age = 18
title = "None"
if age >= 18:
    title = "Adult"
else:
    title = "Minor"

Nested Example:

age = 18
title = "None"
allowed_to_drink = False
if age >= 18:
    title = "Adult"
    if age >= 21:
        allowed_to_drink = True
    else:
        allowed_to_drink = False
else:
    title = "Minor"

The second if-else only executes when the first condition is True.
"""

# Challenge - Beginner
# Write a program that determines eligibility for a movie based on age and parental guidance.
# Your program should:
# 1. Create a variable age and assign it a value from input.
# 2. Create a variable with_parent and assign it a True/False value from input.
# 3. Create a variable named message with the value "None".
# 4. Use nested if-else to determine what string to put in message.

# Get age as an integer
age = int(input())

# Get parental guidance as a boolean (True/False)
with_parent = input() == "true"

# Declare a variable named message with "None"
message = "None"

# Nested if-else logic
if age < 18:
    if with_parent == True:
        message = "You can watch PG-13 movies"
    elif with_parent == False:
        message = "You can only watch G-rated movies"
else:
    message = "You can watch any movie"

# Don't change below this line
print(message)
