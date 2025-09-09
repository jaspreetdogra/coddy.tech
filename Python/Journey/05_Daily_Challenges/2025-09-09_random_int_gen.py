# Daily Challenge - 09/09/2025
# Challenge: Random Integer Generator
#
# Write a function named random_int that takes two integers, a and b,
# and returns a random integer within the range of a and b (inclusive).
#
# Example:
# random_int(5, 9) could return 5, 6, 7, 8, or 9.
#
# Note: Don't call the function, we do that for you ;)

import random

def random_int(a, b):
    return random.randint(a, b)
