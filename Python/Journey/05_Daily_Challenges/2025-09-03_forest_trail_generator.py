"""
Daily Challenge - 3rd September 2025
------------------------------------
Forest Trail Name Generator

Description:
This program generates unique and evocative trail names by combining 
each adjective with each noun from the provided arrays.

Example:
adjectives = ["tranquil", "mystic"]
nouns = ["path", "grove"]

Output:
["tranquil path", "tranquil grove", "mystic path", "mystic grove"]

Learning Goals:
- Function definition
- Nested loops
- List building
- String formatting with f-strings
"""

def generate_trail_names(adjectives, nouns):
    """
    Generates unique trail names by combining adjectives with nouns.
    
    Parameters:
        adjectives (list of str): Descriptive words (e.g., "mystic", "silent").
        nouns (list of str): Nature-related nouns (e.g., "path", "grove").
    
    Returns:
        list of str: All adjective-noun combinations.
    """
    return [f"{adj} {noun}" for adj in adjectives for noun in nouns]


# Example usage (can be removed when integrating into a larger project)
if __name__ == "__main__":
    adjectives = ["tranquil", "mystic"]
    nouns = ["path", "grove"]
    
    result = generate_trail_names(adjectives, nouns)
    print("Generated Trail Names:")
    for name in result:
        print("-", name)
