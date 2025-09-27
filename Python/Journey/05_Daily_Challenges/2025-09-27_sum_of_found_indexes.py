"""
Sum of Found Indexes Challenge
==============================

📌 Problem:
Create a function named `indexes_sum` that takes a list of numbers and a target number. 
The function should return the sum of all indexes in the list where the target number is found. 

⚠️ Conditions:
- If there are no matches, return 0
- If the only match is at index 0, return 0

Example:
--------
indexes_sum([1, 2, 3, 2], 2) → 4   (indexes 1 + 3)
indexes_sum([1, 3, 5, 8, 12], 1) → 0   (only at index 0)
indexes_sum([9, 9, 1, 3, 6, 9, 2, 3], 9) → 6   (indexes 0,1,5 → condition applies → 6)
"""

def indexes_sum(lst, target):
    """
    Returns the sum of all indexes where `target` appears in the list `lst`.

    Parameters:
    -----------
    lst : list[int]
        A list of integers to search through.
    target : int
        The number to search for in the list.

    Returns:
    --------
    int
        The sum of all indexes where the target is found, 
        or 0 if the only match is at index 0 or no matches exist.
    """
    
    # Collect all indexes where target is found
    indices = [i for i, val in enumerate(lst) if val == target]
    
    # Handle edge cases
    if not indices:        # No matches
        return 0
    if indices == [0]:     # Only match is at index 0
        return 0
    
    # Sum all found indexes
    return sum(indices)


# ------------------------------------------------------------
# ✅ Example Test Runs (can be removed in production)
# ------------------------------------------------------------
if __name__ == "__main__":
    print(indexes_sum([1, 2, 3, 2], 2))        # Expected: 4
    print(indexes_sum([1, 3, 5, 8, 12], 1))    # Expected: 0
    print(indexes_sum([9, 9, 1, 3, 6, 9, 2, 3], 9))  # Expected: 6
    print(indexes_sum([9, 9, 1, 3, 6, 9, 2, 3], 3))  # Expected: 10
    print(indexes_sum([9, 9, 1, 3, 6, 9, 2, 3], 4))  # Expected: 0
