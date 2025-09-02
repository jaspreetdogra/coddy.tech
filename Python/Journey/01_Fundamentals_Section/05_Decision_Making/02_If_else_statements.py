"""
If - Else Statements in Python

Theory:

if allows us to execute particular code if a condition is met, 
but if we want to execute something else when the condition is not met, we use else.

Example:

age = 15
status = "None"
if age >= 18:
    status = "Adult"
else:
    status = "Young"

We can also use elif to check multiple conditions:

age = 68
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"

Syntax:
if condition:
    code
elif condition2:
    code
else:
    code

Note: All code inside if/elif/else must be indented.
"""

# Quiz:
# What will be the value of status if age is 20 according to the provided code?

age = 20
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"

# Expected output: Adult
print(f"Quiz output - status = {status}")

# Challenge - Beginner
# You are given a code which gets as input a number that indicates the wind speed
# and stores it in a variable named wind.
# Your task is to initialize variable 'status' based on the conditions:
# "Calm" if wind is smaller than 8,
# "Breeze" if wind is between 8 and 31 (including 8 and 31)
# "Gale" if wind is between 32 and 63 (including 32 and 63)
# "Storm" otherwise

wind = int(input("Enter wind speed: "))  # Don't change this line
status = "unset"

# Solution
if wind < 8:
    status = "Calm"
elif wind >= 8 and wind <= 31:
    status = "Breeze"
elif wind >= 32 and wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")
