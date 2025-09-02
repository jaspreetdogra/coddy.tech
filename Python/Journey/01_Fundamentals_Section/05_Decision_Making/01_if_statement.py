"""
If Statement

If statements allow us to execute code with conditions.

For example, let's look at the following code:
"""

# Example 1
age = 20
status = "Child"
if age > 18:
    status = "Adult"
age += 1

"""
The above code checks whether the age variable is greater than 18.
If it is, it will set status to hold "Adult" string.

In the end, the code will increment age by 1 whether the age is greater than 18 or not.
"""

"""
To use an if statement, we need to add a colon : at the end of the if,
and everything that is inside the if is indented with 4 spaces or tab:

if condition:
    code
    code
    code

If the condition is True, we will enter the code block inside the if (the indented code).
"""

# Quiz
# How do you correctly write an if statement in Python?
# 1. if (condition):
# 2. if condition begin
# 3. if condition then:
# 4. if condition:

"""
Challenge
Beginner

The variables a and b have missing values, fill them so that the code inside
the if statement will be executed! (make sure the if condition is true)

At the end of the program, the value of c should be 3.

Bonus: try to find more than one solution!
"""

# Challenge Solution
a = 12
b = 11

# Don't change below this line
c = 0
if a >= b and not b < 10:
    c = 2

c += 1
print(f"c = {c}")
