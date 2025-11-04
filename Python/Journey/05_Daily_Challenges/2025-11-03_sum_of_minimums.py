def sum_minimums(matrix):
    """
    Sum of Minimums 🧮
    -----------------
    This function takes a 2D list (matrix) as input and returns the sum 
    of the smallest element from each row.
    
    Example:
        [[1, 2, 3, 4, 5],
         [5, 6, 7, 8, 9],
         [20, 21, 34, 56, 100]]
         
        Minimums → [1, 5, 20]
        Sum → 26
    """

    # Initialize a variable to store the total sum
    total_sum = 0

    # Loop through each row in the matrix
    for row in matrix:
        # Find the minimum value in the current row
        min_value = min(row)

        # Add the minimum value to the total sum
        total_sum += min_value

    # Return the final sum of all row minimums
    return total_sum
