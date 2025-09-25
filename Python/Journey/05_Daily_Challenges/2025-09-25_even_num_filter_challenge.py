# Even Number Filter Challenge
# Difficulty: Easy
# Author: Your Name

# Function: filter_even_numbers
# Description:
#   Takes a list of numbers as input.
#   Returns a new list containing only the even numbers,
#   using list comprehension in just 2 lines.

def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# ------------------------
# Example Test Cases
# ------------------------
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))   # [2, 4, 6]
print(filter_even_numbers([10, 11, 13, 16, 18])) # [10, 16, 18]
print(filter_even_numbers([1, 3, 5]))            # []
