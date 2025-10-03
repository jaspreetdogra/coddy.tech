def manage_inventory(inventory, to_remove, range_to_view):
    """
    Function: manage_inventory
    --------------------------
    Manages a shop's inventory by removing a specific item and 
    returning a slice of the updated inventory.

    Parameters:
    inventory (list): List of strings representing the current stock items.
    to_remove (str): The item to be removed from the inventory.
    range_to_view (list): A list of two integers [start, end] 
                          representing the inclusive range for slicing.

    Returns:
    list: A slice of the updated inventory list.
    """

    # Step 1: Remove all instances of `to_remove` from the inventory
    # Using list comprehension to filter out items that are not equal to `to_remove`
    updated_inventory = [item for item in inventory if item != to_remove]

    # Step 2: Extract slicing range
    # Since Python slicing is exclusive at the end, we add +1 to include it
    start, end = range_to_view

    # Step 3: Return the required slice of the updated inventory
    return updated_inventory[start:end + 1]


# ------------------------------
# Example Usage / Test Cases
# ------------------------------
if __name__ == "__main__":
    # Test 1: Removing "apple" and viewing range [0, 1]
    print(manage_inventory(["apple", "banana", "apple", "orange"], "apple", [0, 1]))
    # Expected Output: ["banana", "orange"]

    # Test 2: Removing "pencil" and viewing range [1, 3]
    print(manage_inventory(["pen", "pencil", "eraser", "pencil", "marker"], "pencil", [1, 3]))
    # Expected Output: ["eraser", "marker"]
