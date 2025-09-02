# Logical Operators Part 1
#
# Logical operators are used to combine conditional statements.
#
# Python has three logical operators:
#
# and
# or
# not
#
# Let's see how the and operator works:
#
# The and operator returns True if both statements are true.
#
# # Create two boolean variables
# x = True
# y = True
#
# # Check if both x and y are True
# result = x and y
#
# After executing the above code, result contains:
#
# True
#
# If one of the values is False, the result will be False:
#
# # Create two boolean variables
# x = True
# y = False
#
# # Check if both x and y are True
# result = x and y
#
# This gives us:
#
# False
#
# Quiz
# Which logical operator is used to check if both operands are True?
# 1 and
# 2 not
# 3 or
#
# Challenge
# Easy
# Complete the code to determine if a person is eligible to drive based on their age and license status.
#
# A person is eligible to drive when:
# They are at least 18 years old AND
# They have a valid driving license
#
# Fill in the blanks with the correct values:
# Fill in the age variable with 20
# Fill in the has_license variable with True
# Fill in the minimum age requirement in the comparison

# --- Demo 1: both True -> result is True
x = True
y = True
result = x and y
print(result)  # Expected: True

# --- Demo 2: one False -> result is False
x = True
y = False
result = x and y
print(result)  # Expected: False

# --- Challenge solution
age = 20
has_license = True

result = age >= 18 and has_license

# Don't change the line below
print("Eligible to drive:", result)
