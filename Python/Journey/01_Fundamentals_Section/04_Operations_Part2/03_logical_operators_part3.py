# Logical Operator 3: Logical Operators Part 3
# -----------------------------------------------------------
# In Python, you can combine multiple conditions using logical
# operators (and, or, not) to create more complex expressions.
#
# Example 1: Check if a number is both positive and even.
number = 6
is_positive = number > 0
is_even = number % 2 == 0
result = is_positive and is_even
print("Example 1:", result)  # True because 6 is positive and even

# Example 2: Direct approach without intermediate variables.
result = number > 0 and number % 2 == 0
print("Example 2:", result)  # True

# Example 3: Using OR to check if at least one condition is true.
number = -4
is_negative_or_odd = number < 0 or number % 2 != 0
print("Example 3:", is_negative_or_odd)  # True because -4 is negative

# -----------------------------------------------------------
# Challenge (Easy)
#
# Write code that checks if a person is eligible to drive.
#
# Conditions for eligibility:
#   - The person is at least 18 years old
#   - The person has a license
#   - The person has insurance
#
# Program requirements:
#   1. Read an integer age from the first line of input
#   2. Read a string has_license from the second line ("true"/"false")
#   3. Read a string has_insurance from the third line ("true"/"false")
#   4. Convert license and insurance inputs to boolean values
#   5. Check all three conditions and store the result in variable `result`
#   6. Print the final result (True or False)
# -----------------------------------------------------------

# Solution Code
age = int(input())
has_license = input().lower() == "true"
has_insurance = input().lower() == "true"

result = has_license and has_insurance and age >= 18

print(result)
