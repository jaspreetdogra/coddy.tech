# Daily Challenge - 12/09/2025
# Problem: Filter out Strings from an Array
# Difficulty: Easy
#
# Create a function named filter_list that takes a list of non-negative integers 
# and strings and returns a new list without the strings.
# The function should maintain the original order of the integers in the list.
#
# Examples:
# filter_list([1, 2, "a", "b"]) ➝ [1, 2]
# filter_list([1, "a", "b", 0, 15]) ➝ [1, 0, 15]
# filter_list([1, 2, "aasf", "1", "123", 123]) ➝ [1, 2, 123]

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]


# --------- Testing Section ---------
if __name__ == "__main__":
    # Example test cases
    print(filter_list([1, 2, "a", "b"]))           # [1, 2]
    print(filter_list([1, "a", "b", 0, 15]))       # [1, 0, 15]
    print(filter_list([1, 2, "aasf", "1", "123", 123]))  # [1, 2, 123]
