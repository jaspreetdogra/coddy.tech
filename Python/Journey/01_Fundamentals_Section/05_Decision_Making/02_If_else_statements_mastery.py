"""
If-Else Statement Mastery - Temperature Challenge

Theory:

if allows us to execute code when a condition is met. 
else allows us to execute code when the condition is NOT met.

elif (else if) allows us to check multiple conditions sequentially.

Example:

age = 20
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

# Challenge - Beginner
# You are given a code which gets as input a number that indicates the temperature in Celsius
# and stores it in a variable named temperature.
# Your task is to initialize variable 'weather' based on the following conditions:
# "Freezing" if temperature is below 0
# "Cold" if temperature is between 0 and 15 (including 0 and 15)
# "Mild" if temperature is between 16 and 25 (including 16 and 25)
# "Hot" otherwise

temperature = int(input("Enter temperature in Celsius: "))  # Don't change this line
weather = "unset"

# Solution
if temperature < 0:
    weather = "Freezing"
elif 0 <= temperature <= 15:
    weather = "Cold"
elif 16 <= temperature <= 25:
    weather = "Mild"
else:
    weather = "Hot"

# Don't change the line below
print(f"weather = {weather}")
