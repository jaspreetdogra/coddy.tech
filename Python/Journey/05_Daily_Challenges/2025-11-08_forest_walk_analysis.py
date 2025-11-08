from collections import Counter
from datetime import datetime

def analyze_forest_walk(observations):
    """
    Forest Walk Analysis 🌳
    Analyzes a list of forest tree observations and returns a detailed summary.
    
    Each line in 'observations' follows this format:
    "Tree_ID | Species | Height(m) | Trunk_Diameter(cm) | Leaf_Color | Time_Observed"
    """

    # STEP 1️⃣: Split the observations string into individual tree records
    trees = [tree.split(' | ') for tree in observations.split('\n')]

    # STEP 2️⃣: Define the list of known Fagaceae species
    fagaceae = ['Oak', 'Beech', 'Chestnut']

    # STEP 3️⃣: Count total trees and unique Fagaceae species observed
    total_trees = len(trees)
    fagaceae_species = set(tree[1] for tree in trees if tree[1] in fagaceae)

    # STEP 4️⃣: Calculate average height and trunk diameter
    heights = [float(tree[2]) for tree in trees]
    diameters = [float(tree[3]) for tree in trees]
    avg_height = sum(heights) / len(heights)
    avg_diameter = sum(diameters) / len(diameters)

    # STEP 5️⃣: Find the most common leaf color using Counter
    leaf_colors = [tree[4] for tree in trees]
    most_common_color = Counter(leaf_colors).most_common(1)[0][0]

    # STEP 6️⃣: Determine the time span of the walk (first → last observation)
    times = [datetime.strptime(tree[5], '%H:%M') for tree in trees]
    time_span = max(times) - min(times)

    # STEP 7️⃣: Identify the tallest tree from the observations
    tallest_tree = max(trees, key=lambda x: float(x[2]))

    # STEP 8️⃣: Format and return a neat textual summary
    summary = f"Forest Walk Summary:\n"
    summary += f"1. Total trees observed: {total_trees}\n"
    summary += f"2. Unique Fagaceae species: {len(fagaceae_species)}\n"
    summary += f"3. Average height: {avg_height:.2f}m, Average trunk diameter: {avg_diameter:.2f}cm\n"
    summary += f"4. Most common leaf color: {most_common_color}\n"
    summary += f"5. Time span of walk: {time_span}\n"
    summary += f"6. Fagaceae species encountered: {', '.join(sorted(fagaceae_species))}\n"
    summary += f"7. Tallest tree: Species: {tallest_tree[1]}, Height: {tallest_tree[2]}m, Trunk Diameter: {tallest_tree[3]}cm"

    return summary
