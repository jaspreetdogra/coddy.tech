# Logical Operators Part 2
# Logical operators have a special table called "Truth table" that shows what the combination of logical operators returns.

# Truth table for the and operator:
# a     b     a and b
# False False False
# False True  False
# True  False False
# True  True  True
# The only way to get a True for the and operator is if both a and b are True

# Truth table for the or operator:
# a     b     a or b
# False False False
# False True  True
# True  False True
# True  True  True
# In this case, to get a True result, either a or b should be True.

# Truth table for the not operator:
# a     not a
# False True
# True  False
# Here the value of a is reversed. If a is False then not a is True

# Challenge
# Beginner
# Replace the values of variables b1 and b2 with numbers so that b3 evaluates to True.
# b3 will be True when the multiplication of b1 and b2 is greater than their addition.

# Replace the values with numbers
b1 = 5
b2 = 4

# This line checks if b1 * b2 is greater than b1 + b2
b3 = (b1 * b2) > (b1 + b2)

# Don't change the line below
print(f"b3 = {b3}")
