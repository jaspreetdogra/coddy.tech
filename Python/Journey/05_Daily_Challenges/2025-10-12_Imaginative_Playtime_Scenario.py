"""
Imaginative Playtime Scenario
-----------------------------

Creator: [Your Name or Username]
Challenge Difficulty: Medium

Description:
------------
Simulate a child's imaginative playtime with toy vehicles and colorful building blocks.
This function performs creative string and list operations to generate a playful scenario.

Steps:
------
1. Reverse the string of colored building blocks.
2. Reverse the list of toy vehicle names.
3. Repeat the reversed block pattern based on the given repetition count.
4. Create a new sequence by *alternating* between:
   - Elements of the reversed vehicle list, and
   - Characters from the concatenated building block string.
5. Join the sequence with spaces to form the final imaginative scene.

Parameters:
-----------
blocks (str): A string representing colored building blocks (e.g., "RYBGPO").
vehicles (list): A list of toy vehicle names (e.g., ["car", "truck", "bus", "train"]).
repetitions (int): Number of times to repeat the block pattern.

Returns:
--------
str: A single string combining reversed vehicles and block characters in an alternating pattern.

Example:
--------
blocks = "RYBGPO"
vehicles = ["car", "truck", "bus", "train"]
repetitions = 2

# Reversed blocks: "OPGBYR"
# Reversed vehicles: ["train", "bus", "truck", "car"]
# Repeated blocks: "OPGBYROPGBYR"

# Alternating example output:
# "train O bus P truck G car B Y R O P G B Y R"

# Final output:
# "train O bus P truck G car B Y R O P G B Y R"
"""

def playtime_scenario(blocks, vehicles, repetitions):
    """
    Create a playful imaginative scenario combining blocks and vehicles.

    Args:
        blocks (str): String representing block colors (e.g., "RYBGPO").
        vehicles (list[str]): List of toy vehicle names.
        repetitions (int): Number of repetitions of the block pattern.

    Returns:
        str: A string describing the imaginative playtime scenario.
    """

    # Step 1: Reverse the blocks string
    reversed_blocks = blocks[::-1]

    # Step 2: Reverse the vehicles list
    reversed_vehicles = vehicles[::-1]

    # Step 3: Repeat the reversed blocks pattern
    repeated_blocks = reversed_blocks * repetitions

    # Step 4: Build alternating sequence
    result = []
    block_index = 0
    vehicle_index = 0

    # Alternate until both sources are exhausted
    while vehicle_index < len(reversed_vehicles) or block_index < len(repeated_blocks):
        if vehicle_index < len(reversed_vehicles):
            result.append(reversed_vehicles[vehicle_index])
            vehicle_index += 1
        if block_index < len(repeated_blocks):
            result.append(repeated_blocks[block_index])
            block_index += 1

    # Step 5: Join elements with spaces
    return ' '.join(result)


# Example usage (for testing)
if __name__ == "__main__":
    blocks = "RYBGPO"
    vehicles = ["car", "truck", "bus", "train"]
    repetitions = 2
    print(playtime_scenario(blocks, vehicles, repetitions))
