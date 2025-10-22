# Challenge: Playground Giggle Counter
# Difficulty: Medium
#
# Guided Material / What to Do:
# Create a function named giggle_counter that receives laughter_string as its parameter.
#
# 🎯 Goal:
# Simulate a playground game called "Giggle Counter".
# Parse a string representation of children's laughter and calculate a score
# based on the intensity and frequency of their giggles.
#
# 🧩 Description:
# - The laughter_string represents multiple children giggling.
# - Each child is identified by a letter (A-Z), followed by ":" and a series of 'h's.
# - Example: "A:hhh B:h C:hhhh A:hh B:hhhhh"
#
# 🧠 Rules for Calculating the Giggle Score:
# 1️⃣ Each 'h' in a giggle = 1 point.
# 2️⃣ If a child giggles multiple times, add +1 for each subsequent giggle.
# 3️⃣ If a giggle is longer than their previous giggle → +1 bonus point.
# 4️⃣ If a giggle is shorter than their previous giggle → -1 penalty point (but score can’t go below 0).
#
# 🧮 Parameters:
# - laughter_string (str): A string representing the laughter of children in the playground.
#
# 🏁 Return:
# - A dictionary where each key is a child’s identifier (A-Z)
#   and the value is their final calculated giggle score.
#
# ⚙️ Constraints:
# - The string will contain 1–200 characters.
# - Each child’s identifier is a single uppercase letter (A–Z).
# - Each giggle only contains 'h' characters.
# - Laughter segments are separated by spaces.
# - The same child may appear multiple times.

def giggle_counter(laughter_string):
    # Initialize a dictionary to store each child’s data:
    # - score: total points
    # - prev_length: length of previous giggle
    # - giggle_count: how many times they’ve giggled
    children = {}

    # Split the laughter string into individual giggle entries
    for laugh in laughter_string.split():
        # Separate the child’s name (e.g., 'A') and their giggle (e.g., 'hhh')
        child, giggle = laugh.split(':')

        # Initialize data for new child if not seen before
        if child not in children:
            children[child] = {'score': 0, 'prev_length': 0, 'giggle_count': 0}

        # Calculate length of the current giggle (intensity)
        current_length = len(giggle)

        # Add 1 point per 'h'
        children[child]['score'] += current_length

        # Increment giggle count
        children[child]['giggle_count'] += 1

        # Add +1 if this is not the first giggle (for multiple giggles)
        if children[child]['giggle_count'] > 1:
            children[child]['score'] += 1

        # Compare current and previous giggle lengths
        if current_length > children[child]['prev_length']:
            # Giggle got longer → +1 bonus
            children[child]['score'] += 1
        elif current_length < children[child]['prev_length']:
            # Giggle got shorter → -1 penalty, but score can’t go below 0
            children[child]['score'] = max(0, children[child]['score'] - 1)

        # Update previous giggle length
        children[child]['prev_length'] = current_length

    # Return only the final scores in a clean dictionary
    return {child: data['score'] for child, data in children.items()}

# 🧪 Example Test:
print(giggle_counter("A:hhh B:h C:hhhh A:hh B:hhhhh"))
# Expected Output: {'A': 7, 'B': 9, 'C': 5}
