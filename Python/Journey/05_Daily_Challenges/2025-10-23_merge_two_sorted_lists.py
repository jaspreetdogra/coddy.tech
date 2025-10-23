# Challenge: Merge Two Sorted Lists
# Difficulty: Medium
#
# 🧭 Guided Material / What to Do:
# Write a function named merge_lists(list_1, list_2) that takes two sorted lists of integers
# and returns a single merged and sorted list.
#
# 🚫 Restrictions:
# - Do NOT use any built-in Python sorting functions (like sorted() or list.sort()).
#
# 🧩 Idea:
# Since both lists are already sorted, we can merge them efficiently
# using a "two-pointer" technique — similar to the merge step in merge sort.
#
# 🧠 Steps to Solve:
# 1️⃣ Initialize two pointers (i and j) at the start of list_1 and list_2.
# 2️⃣ Compare elements at both pointers:
#     - If list_1[i] <= list_2[j], append list_1[i] to result and move i forward.
#     - Else, append list_2[j] and move j forward.
# 3️⃣ When one list is exhausted, append all remaining elements from the other list.
# 4️⃣ Return the merged result list.
#
# 🧮 Parameters:
# - list_1 (list[int]): First sorted list of integers.
# - list_2 (list[int]): Second sorted list of integers.
#
# 🏁 Return:
# - A single list[int] containing all elements from both lists, merged in sorted order.
#
# 🧪 Example:
# merge_lists([1, 3, 5], [2, 4, 6])
# ➜ [1, 2, 3, 4, 5, 6]

def merge_lists(list_1, list_2):
    # Initialize empty list for the merged result
    merged_list = []
    
    # Initialize two pointers for both lists
    i, j = 0, 0

    # Merge while both lists have elements remaining
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    # Append remaining elements (if any) from list_1
    while i < len(list_1):
        merged_list.append(list_1[i])
        i += 1

    # Append remaining elements (if any) from list_2
    while j < len(list_2):
        merged_list.append(list_2[j])
        j += 1

    # Return the fully merged and sorted list
    return merged_list

# 🧪 Example Test:
print(merge_lists([1, 3, 5], [2, 4, 6]))   # Expected Output: [1, 2, 3, 4, 5, 6]
print(merge_lists([10, 20, 30], [5, 15, 25, 35]))  # Expected Output: [5, 10, 15, 20, 25, 30, 35]
