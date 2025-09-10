# 2025-09-09 Daily Challenge
# Next Element in Arithmetic Sequence
#
# Write a function named next_element that gets a list of numbers representing
# an arithmetic sequence and returns the next element in the sequence.
#
# Examples:
# next_element([3, 5, 7, 9]) -> 11
# next_element([-5, -6, -7]) -> -8
# next_element([2, 2, 2, 2, 2]) -> 2

def next_element(seq):
    # Common difference = second element - first element
    diff = seq[1] - seq[0]
    return seq[-1] + diff
