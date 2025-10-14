def calculate_average_weight(weights):
    # Challenge
    # Medium
    #
    # Create a function named calculate_average_weight that receives a list of weights called weights.
    # The function will calculate the average weight of the herd based on the provided weights list.
    #
    # If the list contains an invalid weight (negative or non-numeric),
    # the function should skip that weight and continue calculating the average using only the valid weights.
    #
    # The function should return a string in the format:
    # "The average weight of the herd is X lbs.",
    # where X is the calculated average weight rounded to 2 decimal places.
    #
    # Note:
    # If the weights list is empty or contains only invalid weights,
    # the function should return: "No valid weights provided."
    #
    # The function should handle exceptions gracefully without raising any errors or stopping the program execution.
    #
    # Example:
    # Input: [100, 150, 200, 250, 300]
    # Output: "The average weight of the herd is 200.00 lbs."

    # Step 1: Initialize a list for valid weights
    valid_weights = []
    
    # Step 2: Loop through each element to validate and collect correct weights
    for w in weights:
        try:
            weight = float(w)  # Try to convert to float
            if weight >= 0:    # Check for non-negative weights
                valid_weights.append(weight)
        except (ValueError, TypeError):
            continue  # Skip invalid entries gracefully
    
    # Step 3: Handle case when no valid weights exist
    if not valid_weights:
        return "No valid weights provided."
    
    # Step 4: Compute average and return formatted result
    average = sum(valid_weights) / len(valid_weights)
    return f"The average weight of the herd is {average:.2f} lbs."
