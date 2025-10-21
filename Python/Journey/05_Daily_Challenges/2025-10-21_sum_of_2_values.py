# Challenge: Sum of Two Values
# Difficulty: Medium
#
# Guided Material / What to Do:
# Write a function sum_of_two_values(arr, target) that takes a list of numbers (arr)
# and a target number (target) as input.
#
# The function should:
# 1️⃣ Return a list containing two numbers that add up to the target number.
# 2️⃣ If no such pair exists, return an empty list.
#
# Example:
# Input: arr = [1, 2, 3, 4, 5, 10], target = 11
# Output: [1, 10]
#
# Constraints:
# - The list may contain integers.
# - Each number can be used only once.
# - The order of the returned pair does not matter.

def sum_of_two_values(arr, target):
    # Create a set to keep track of numbers we've already seen
    seen = set()

    # Iterate through each number in the list
    for num in arr:
        # Find the number that would complete the pair to reach the target
        complement = target - num

        # If the complement exists in the seen set, return the pair as a list
        if complement in seen:
            return [complement, num]

        # Add the current number to the seen set for future checks
        seen.add(num)

    # If no pair adds up to the target, return an empty list
    return []

# Example test
print(sum_of_two_values([1, 2, 3, 4, 5, 10], 11))  # Expected Output: [1, 10]
