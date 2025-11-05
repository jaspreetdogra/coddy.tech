def select_horse_breeds(breeds, start, end):
    """
    🐎 Horse Breed Selection at the Ranch
    
    Challenge Level: Beginner
    
    Guided Steps:
    1. The function receives:
       - `breeds`: a list of horse breed names.
       - `start`: the starting index (inclusive).
       - `end`: the ending index (exclusive).
    2. We need to simulate visitors selecting a range of horse breeds.
    3. Use Python’s list slicing to return a subset of the list.
       Syntax: list[start:end] → includes start, excludes end.
    4. Return the sliced portion as the selected breeds.
    """

    # Extract the desired slice of the breeds list using slicing
    selected_breeds = breeds[start:end]
    
    # Return the resulting sublist
    return selected_breeds
