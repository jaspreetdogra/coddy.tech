# -----------------------------------------------------------
# Challenge: Office Routine Shuffle: A Day of Overrides
# Difficulty: Medium
#
# Guided Material / Instructions:
#
# Create a function named office_routine_shuffle that receives:
#   - routines (list of lists of strings): represents daily tasks for employees
#   - shuffle_count (int): number of times to shuffle the routines
#   - special_tasks (list of strings): extra tasks to be inserted
#
# The function should:
#   1. Reverse the order of routines for each employee (WITHOUT using reverse() or slicing).
#   2. Concatenate the reversed routines with the original routines for each employee.
#   3. Insert special tasks into the concatenated routines using this formula:
#        position = (task_index * employee_index) % len(concatenated_routine)
#   4. Repeat steps 1-3 for 'shuffle_count' times.
#   5. Return the final shuffled routines (2D list).
#
# Note:
# - Implement your own reversing logic using loops.
# - Use modular arithmetic carefully for inserting tasks.
# - The final result should be a list of lists of strings.
#
# Example:
# routines = [["emails", "meeting", "coding"], ["report", "call", "review"]]
# shuffle_count = 1
# special_tasks = ["lunch", "break"]
#
# Expected Output (may vary slightly depending on task placement):
# [
#   ['coding', 'meeting', 'emails', 'emails', 'meeting', 'coding', 'lunch', 'break'],
#   ['review', 'call', 'report', 'report', 'call', 'review', 'lunch', 'break']
# ]
# -----------------------------------------------------------

def office_routine_shuffle(routines, shuffle_count, special_tasks):
    # Function to reverse a list manually
    def reverse_list(lst):
        reversed_list = []
        for i in range(len(lst) - 1, -1, -1):
            reversed_list.append(lst[i])
        return reversed_list

    # Perform the shuffle process 'shuffle_count' times
    for _ in range(shuffle_count):
        new_routines = []

        # Iterate through each employee's routine
        for emp_index, emp_tasks in enumerate(routines):
            # Step 1: Reverse employee tasks
            reversed_tasks = reverse_list(emp_tasks)

            # Step 2: Concatenate reversed + original
            combined = reversed_tasks + emp_tasks

            # Step 3: Insert special tasks
            for task_index, task in enumerate(special_tasks):
                if len(combined) == 0:
                    continue
                position = (task_index * emp_index) % len(combined)
                combined.insert(position, task)

            # Append updated routine to new_routines
            new_routines.append(combined)

        # Update routines for the next shuffle
        routines = new_routines

    # Return the final shuffled routines
    return routines


# ---------------- Example Run ----------------
routines = [["emails", "meeting", "coding"], ["report", "call", "review"]]
shuffle_count = 1
special_tasks = ["lunch", "break"]

print(office_routine_shuffle(routines, shuffle_count, special_tasks))
