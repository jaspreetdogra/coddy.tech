"""
Captain's Nameplate Makeover 🚢
--------------------------------
This script contains the function `redecorate_ship_name`, which redecorates a ship's name
according to specific transformation rules.

Challenge Summary:
1. Reverse the entire ship name.
2. For each word in the reversed name:
   - If it starts with a vowel (a, e, i, o, u), keep it as is.
   - If it starts with a consonant, remove all vowels from that word.
3. Stop processing when encountering the word "dock" (case-insensitive).
4. Use loop control statements like `break` and `continue`.
"""

def redecorate_ship_name(ship_name):
    """
    Redecorates a ship name following specific vowel/consonant rules.

    Parameters:
        ship_name (str): The name of the ship (1 <= len(ship_name) <= 100)

    Returns:
        str: The redecorated ship name after applying all transformation rules.
    """
    vowels = 'aeiouAEIOU'

    # Step 1: Reverse the entire ship name
    reversed_name = ship_name[::-1]

    # Step 2: Split into individual words
    words = reversed_name.split()

    # Step 3: Process each word according to rules
    result_words = []
    for word in words:
        # Stop if "dock" is found (case-insensitive)
        if word.lower() == "dock":
            break

        # If word starts with a vowel, keep as is
        if word[0] in vowels:
            result_words.append(word)
        else:
            # Remove all vowels if word starts with a consonant
            new_word = ''.join([ch for ch in word if ch not in vowels])
            result_words.append(new_word)

    # Step 4: Join processed words back into a string
    return ' '.join(result_words)


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    examples = [
        "Sea Voyager",
        "Ocean Dockyard",
        "Galactic Dock Hunter",
        "Underwater Explorer"
    ]

    for name in examples:
        redecorated = redecorate_ship_name(name)
        print(f"Original: {name}\nRedecorated: {redecorated}\n")
