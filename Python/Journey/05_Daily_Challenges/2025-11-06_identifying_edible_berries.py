def identify_edible_berries(berries):
    """
    Identifying Edible Berries 🍓

    Challenge:
    Create a function that filters and returns only edible berries 
    from a given list of berry names encountered during a hike.

    Parameters:
    berries (list of str): A list containing names of berries encountered.

    Returns:
    list of str: A new list containing only the names of edible berries.
    """

    # Step 1: Define the list of known edible berries
    edible_list = [
        "raspberry", "blueberry", "blackberry", "strawberry", "elderberry",
        "cranberry", "mulberry", "huckleberry", "gooseberry", "currant",
        "boysenberry", "loganberry", "juniper berry"
    ]

    # Step 2: Initialize an empty list to store edible berries found
    edible_berries = []

    # Step 3: Loop through each berry from the input list
    for berry in berries:
        # Step 4: Convert to lowercase for consistent comparison
        if berry.lower() in edible_list:
            edible_berries.append(berry)

    # Step 5: Return the list of identified edible berries
    return edible_berries
