# ======================================================
# Project: Highest Digit Finder
# Description:
# This project contains a function `highest_digit` that
# takes a number as input and returns the highest digit
# in that number. Demonstrates iteration over strings
# and use of the max() function.
# ======================================================

# Function to find the highest digit in a number
def highest_digit(number):
    """
    Returns the highest digit in the given number.

    Parameters:
    number (int): The number to process

    Returns:
    int: The highest digit in the number
    """
    # Convert the number to a string to iterate over each digit
    number_str = str(abs(number))  # Use abs() to handle negative numbers
    
    # Use max() to find the largest character (digit) and convert back to int
    max_digit = int(max(number_str))
    
    return max_digit

# ---------------------- Test Cases ----------------------
# Example usages of the function

print(highest_digit(379))      # Expected output: 9
print(highest_digit(2))        # Expected output: 2
print(highest_digit(377401))   # Expected output: 7
print(highest_digit(-8465))    # Expected output: 8 (negative number support)
print(highest_digit(0))        # Expected output: 0
