"""
If Statement Mastery

Challenge
Beginner

The variables a and b have missing values. Fill them so that the code inside
the if statement will be executed! (make sure the if condition is true)

At the end of the program, the value of c should be 3.

Bonus: try to find more than one solution!
"""

# Initialize variables
a = 5
b = 12   # One possible solution (b >= 10 makes condition True)

# Don't change below this line
c = 0
if a < b or b >= 10:
    c = 2

c += 1
print(f"c = {c}")
