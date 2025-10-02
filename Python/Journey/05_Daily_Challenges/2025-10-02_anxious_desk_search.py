"""
Daily Coding Challenge 🚀
-------------------------

📌 Challenge: Anxious Desk Search
Difficulty: Easy

📝 Description:
You are a nervous officeholder on your first day at work. In your anxiety, you 
reorganize your desk in reverse order and then frantically search for a target item. 

Implement a function that:
1. Reverses the order of items in the desk_items list (without using reverse()).
2. Searches for the target_item in the reversed list (without using index()).
3. Returns the index of target_item if found, else -1.

📌 Function to implement:
anxious_desk_search(desk_items: list[str], target_item: str) -> int
"""

# -----------------------------------------------------------
# ✅ Solution
# -----------------------------------------------------------

def anxious_desk_search(desk_items, target_item):
    """
    Simulates anxious desk search by reversing the desk and finding the target item.
    
    Parameters:
    - desk_items (list of str): The items on the desk
    - target_item (str): The item to search for
    
    Returns:
    - int: Index of target_item in reversed desk, or -1 if not found
    """
    # Step 1: Reverse desk_items manually (no reverse())
    reversed_items = []
    for i in range(len(desk_items) - 1, -1, -1):
        reversed_items.append(desk_items[i])

    # Step 2: Search for target_item manually (no index())
    for i in range(len(reversed_items)):
        if reversed_items[i] == target_item:
            return i

    # If not found
    return -1


# -----------------------------------------------------------
# ✅ Example Usage / Test Cases
# -----------------------------------------------------------

if __name__ == "__main__":
    desk = ["pen", "notebook", "stapler", "coffee", "phone"]
    
    print(anxious_desk_search(desk, "coffee"))  
    # Expected Output: 1 (since reversed desk = ["phone", "coffee", "stapler", "notebook", "pen"])
    
    print(anxious_desk_search(desk, "laptop"))  
    # Expected Output: -1
