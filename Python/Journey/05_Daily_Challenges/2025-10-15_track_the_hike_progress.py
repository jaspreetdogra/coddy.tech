def track_hike_progress(altitude_list):
    # Challenge
    # Easy
    #
    # Create a function named track_hike_progress that receives altitude_list as its parameter.
    #
    # This function tracks your hike progress by counting the number of ascents and descents.
    #
    # Steps to follow:
    # 1. Initialize ascents and descents to 0.
    # 2. Iterate through altitude_list from index 1 to the end.
    # 3. Compare each altitude with the previous one:
    #    - Increment ascents if the current altitude is higher.
    #    - Increment descents if the current altitude is lower.
    # 4. Create and return a dictionary with keys "ascents" and "descents".
    #
    # Parameters:
    # altitude_list (list): A list of integers representing the altitude at each step.
    #
    # The function returns a dictionary with:
    # "ascents" (int): Number of ascents.
    # "descents" (int): Number of descents.
    #
    # Example:
    # Input: [100, 120, 115, 130, 125]
    # Output: {'ascents': 2, 'descents': 2}

    # Step 1: Initialize counters
    ascents = 0
    descents = 0

    # Step 2: Loop through altitudes from the second element
    for i in range(1, len(altitude_list)):
        # Step 3: Compare with previous altitude
        if altitude_list[i] > altitude_list[i - 1]:
            ascents += 1
        elif altitude_list[i] < altitude_list[i - 1]:
            descents += 1

    # Step 4: Return result as dictionary
    return {"ascents": ascents, "descents": descents}
