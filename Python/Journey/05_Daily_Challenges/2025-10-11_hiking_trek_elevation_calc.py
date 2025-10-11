def calculate_trek_elevation(elevation_points):
    """
    Calculates total ascent and descent based on elevation points.

    Parameters:
        elevation_points (list[int]): A list of elevation points representing
                                      heights at consecutive steps of the trek.

    Returns:
        tuple[int, int]: A tuple containing:
            - total_ascent (int): Total gain in elevation.
            - total_descent (int): Total loss in elevation (absolute value).
    """

    total_ascent = 0
    total_descent = 0

    # Loop through each pair of consecutive elevation points
    for i in range(1, len(elevation_points)):
        # Calculate elevation difference between consecutive points
        change = elevation_points[i] - elevation_points[i - 1]

        # If the change is positive, add to ascent
        if change > 0:
            total_ascent += change
        # If the change is negative, add absolute value to descent
        elif change < 0:
            total_descent += abs(change)
        # No change means flat — skip (continue statement for clarity)
        else:
            continue

    # Return the results as a tuple
    return (total_ascent, total_descent)
