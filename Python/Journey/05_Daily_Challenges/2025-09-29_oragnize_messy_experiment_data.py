"""
Daily Coding Challenge 🚀
-------------------------
Challenge: Organize Messy Experiment Data
Difficulty: Easy

📝 Problem Statement:
A frustrated researcher needs help organizing their messy experimental data.  
Your task is to create a function that sorts and processes the raw data to make it more presentable and easier to analyze.

Requirements:
1. Sort the input array in ascending order.
2. Remove any duplicate values from the sorted array.
3. Calculate the average (mean) of the unique values.
4. Return a new array containing:
   - A sorted list of unique values
   - The count of unique values
   - The average of unique values, rounded to 2 decimal places

📥 Parameters:
- raw_data (list[int]): 
    An array of integers (length 1 to 100, values between 0–1000).

📤 Returns:
- list: [sorted_unique_values, count, average]
"""

def organize_experiment_data(raw_data):
    """
    Organizes messy experimental data by:
    - Sorting values in ascending order
    - Removing duplicates
    - Calculating average of unique values

    Args:
        raw_data (list[int]): Input list of integers

    Returns:
        list: [sorted unique values, count of unique values, average rounded to 2 decimals]
    """
    # 1. Remove duplicates and sort
    unique_sorted = sorted(set(raw_data))

    # 2. Count unique values
    count = len(unique_sorted)

    # 3. Calculate average (rounded to 2 decimals)
    avg = round(sum(unique_sorted) / count, 2)

    # 4. Return as per requirements
    return [unique_sorted, count, avg]


# ✅ Example Usage / Test Cases
if __name__ == "__main__":
    print(organize_experiment_data([5, 3, 8, 3, 5, 10]))
    # Expected: [[3, 5, 8, 10], 4, 6.5]

    print(organize_experiment_data([100, 100, 100]))
    # Expected: [[100], 1, 100.0]

    print(organize_experiment_data([1]))
    # Expected: [[1], 1, 1.0]
