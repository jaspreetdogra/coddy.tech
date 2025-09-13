"""
Daily Challenge - 12/9/25
Remove Duplicate Elements from an Array

Challenge:
Write a function remove_duplicates(in_list) that takes a list of integers in_list
and returns a new list with duplicates removed. The order of elements should remain
the same as in the input list.

Example:
remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
"""

def remove_duplicates(in_list):
    """
    Remove duplicate integers from a list while maintaining the original order.
    
    Args:
        in_list (list): List of integers (may contain duplicates)
    
    Returns:
        list: New list with duplicates removed
    """
    seen = set()
    result = []
    for num in in_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example usage / testing
if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 1, 4, 5, 3]
    print("Original list:", test_list)
    print("After removing duplicates:", remove_duplicates(test_list))
