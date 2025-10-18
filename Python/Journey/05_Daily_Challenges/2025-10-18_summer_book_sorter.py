def summerBookSorter(chapters):
    # Challenge
    # Medium
    #
    # Create a function named summerBookSorter that receives chapters as its parameter.
    #
    # This function aims to simulate organizing a list of book chapters during a lazy summer afternoon. 
    # Given an input 2D array where each nested list represents a set of page numbers in a chapter, 
    # the function should perform the following operations:
    #
    # 1. Reverse the order of chapters in each nested list one by one.
    # 2. Sort each nested list in descending order.
    # 3. Combine elements across nested lists based on their positions — that is, 
    #    sum up the elements at the same index across all nested lists.
    #
    # The function should return a new 2D integer array with the combined and sorted chapters.
    #
    # Parameters:
    # chapters (list of list of int): 
    #     A 2D integer array where each nested list represents a set of page numbers in a chapter.
    #
    # Returns:
    # list of list of int: 
    #     A 2D integer array where each nested list has been reversed, sorted in descending order, 
    #     and then combined with others based on the indices of their elements.
    #
    # Example:
    # Input:
    # chapters = [
    #     [1, 3, 5],
    #     [2, 4, 6],
    #     [7, 9, 11]
    # ]
    #
    # Step 1 → Reverse each chapter:
    #     [[5, 3, 1], [6, 4, 2], [11, 9, 7]]
    #
    # Step 2 → Sort each chapter in descending order (already reversed above, so same result):
    #     [[5, 3, 1], [6, 4, 2], [11, 9, 7]]
    #
    # Step 3 → Combine elements across chapters (sum by index):
    #     [
    #         [5 + 6 + 11, 3 + 4 + 9, 1 + 2 + 7]
    #     ] → [[22, 16, 10]]
    #
    # Step 4 → Sort combined list in descending order (optional depending on final requirement)
    #     [[22, 16, 10]]
    #
    # Output:
    # [[22, 16, 10]]
    #
    # Edge Cases to Consider:
    # - Empty input list (should return [])
    # - Uneven sublist lengths (missing positions treated as 0 during combination)
    # - Single chapter (should still reverse and sort properly)

    # Step 1: Handle edge case — empty list
    if not chapters:
        return []

    # Step 2: Reverse and sort each chapter in descending order
    processed = [sorted(ch[::-1], reverse=True) for ch in chapters]

    # Step 3: Find the maximum length among all chapters to handle uneven lengths
    max_len = max(len(ch) for ch in processed)

    # Step 4: Initialize a list to hold combined sums
    combined = [0] * max_len

    # Step 5: Combine elements by their positions across all chapters
    for ch in processed:
        for i in range(len(ch)):
            combined[i] += ch[i]

    # Step 6: Wrap combined list inside another list (to maintain 2D array format)
    # and sort it in descending order
    return [sorted(combined, reverse=True)]
