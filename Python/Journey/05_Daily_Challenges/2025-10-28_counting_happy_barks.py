# -----------------------------------------------------------
# Challenge: Counting Happy Barks in the Sunny Backyard
# Difficulty: Easy
#
# Guided Material / Instructions:
#
# Create a function named count_happy_barks that receives:
#   - backyard_sounds (str): a string representing all the sounds made 
#     by dogs in the sunny backyard.
#
# Task:
#   Count the number of *happy barks* in the given string.
#
# Definition:
#   A "happy bark" is the substring "woof!" (that is, the bark "woof"
#   immediately followed by an exclamation mark).
#
# Implementation Details:
#   1. Initialize a counter (happy_bark_count) to zero.
#   2. Use a while loop to iterate through the backyard_sounds string.
#   3. At each index, check if the substring starting from that index 
#      equals "woof!".
#   4. If yes, increment the counter and move the index forward by 5 
#      (the length of "woof!").
#   5. Otherwise, move the index forward by 1.
#   6. Continue until reaching the end of the string.
#   7. Return the total count of happy barks.
#
# Notes:
#   - This approach handles overlapping occurrences correctly.
#   - Stops efficiently when no further "woof!" can fit in the remaining string.
#
# Example:
#   Input:  "woof! woof woof!woof!"
#   Output: 3
# -----------------------------------------------------------

def count_happy_barks(backyard_sounds):
    happy_bark_count = 0   # Step 1: initialize counter
    i = 0                  # Step 2: starting index
    
    # Step 3: iterate through string while at least 5 characters remain
    while i < len(backyard_sounds) - 4:
        # Step 4: check for "woof!"
        if backyard_sounds[i:i+5] == "woof!":
            happy_bark_count += 1
            i += 5  # Step 5: skip past this bark
        else:
            i += 1  # move to next character
    
    # Step 6: return total count
    return happy_bark_count


# ---------------- Example Run ----------------
print(count_happy_barks("woof! woof woof!woof!"))  # Expected Output: 3
