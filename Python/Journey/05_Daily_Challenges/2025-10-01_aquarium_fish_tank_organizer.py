"""
Daily Coding Challenge 🚀
-------------------------

📌 Challenge: Aquarium Fish Tank Organizer
Difficulty: Easy

📝 Description:
You are given a list of fish counts in different tanks.
Your task is to sort the tanks from the least number of fish to the most.
If a tank has more than 50 fish, mark it as "crowded".

📌 Function to implement:
sort_fish_tanks(fish_counts: list[int]) -> list[str]
⚠️ Constraints:
- Each fish count is an integer between 1 and 100
- List can contain 1 to 100 tanks
"""

# -----------------------------------------------------------
# ✅ Solution
# -----------------------------------------------------------

def sort_fish_tanks(fish_counts):
    """
    Organizes fish tanks by number of fish.
    
    Parameters:
    - fish_counts (list of int): Number of fish in each tank
    
    Returns:
    - list of str: Sorted fish counts with crowded tanks marked
    """
    # Step 1: Sort the fish counts in ascending order
    sorted_counts = sorted(fish_counts)

    # Step 2: Create formatted list with crowded note if fish > 50
    result = []
    for count in sorted_counts:
        if count > 50:
            result.append(f"{count} (crowded)")
        else:
            result.append(f"{count}")
    
    return result


# -----------------------------------------------------------
# ✅ Example Usage / Test Cases
# -----------------------------------------------------------

if __name__ == "__main__":
    tanks = [10, 75, 45, 55, 20]
    organized_tanks = sort_fish_tanks(tanks)
    print(organized_tanks)
    # Expected Output: ['10', '20', '45', '55 (crowded)', '75 (crowded)']
