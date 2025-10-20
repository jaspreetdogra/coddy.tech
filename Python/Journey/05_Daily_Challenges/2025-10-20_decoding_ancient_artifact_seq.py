def decode_artifact_sequence(encoded_sequence):
    # Challenge
    # Medium
    #
    # Create a function named decode_artifact_sequence that receives encoded_sequence as its parameter.
    #
    # In a scientist's laboratory filled with unusual specimens and ancient artifacts, 
    # an advanced decoding tool is needed to unravel the mysteries of newly discovered relics. 
    # Your task is to create a function that decodes a sequence of symbols and binary numbers, 
    # revealing hidden messages from the past.
    #
    # The function should perform the following steps:
    #
    # 1. Split the input string into groups based on special characters (@, #, $, %, ^, &, *).
    #
    # 2. Process each group as follows:
    #    - If the group is a valid binary number, convert it to decimal.
    #    - If it's not a binary number, keep it as is.
    #
    # 3. Use nested loops to process the converted groups:
    #    - Outer loop: Iterate through the groups.
    #    - Inner loop: Process each character in the group.
    #
    # 4. Apply the following decoding rules:
    #    - If the group was originally a binary number:
    #         → Convert the decimal value to its corresponding ASCII character.
    #    - If the group was not a binary number:
    #         → Shift each character in the group by 1 position in the alphabet 
    #           (e.g., 'A' becomes 'B', 'Z' becomes 'A').
    #
    # 5. Concatenate all decoded parts to form the final message.
    #
    # Parameters:
    # encoded_sequence (str): 
    #     A string containing a mixture of symbols and binary numbers, 
    #     separated by special characters.
    #
    # Returns:
    # str: 
    #     A decoded message revealing the hidden information.
    #
    # Constraints:
    # - The input string will contain only uppercase letters, digits (0 and 1), 
    #   and special characters (@, #, $, %, ^, &, *).
    # - Binary numbers in the input will always be 8 bits long.
    # - Non-binary groups will contain only uppercase letters.
    # - The input string will have a maximum length of 1000 characters.
    #
    # Example:
    # Input:
    # "01001000@01000101#LLO"
    #
    # Step 1 → Split by special characters:
    # ['01001000', '01000101', 'LLO']
    #
    # Step 2 → Decode each group:
    # - '01001000' → binary → decimal 72 → ASCII 'H'
    # - '01000101' → binary → decimal 69 → ASCII 'E'
    # - 'LLO' → letters → shift each by +1 → 'MMO'
    #
    # Step 3 → Concatenate → "HEMMO"
    #
    # Output:
    # "HEMMO"
    #
    # Edge Cases:
    # - Empty string should return an empty string.
    # - Invalid binary groups should be skipped or treated as normal text.
    # - Ensure wrapping for 'Z' → 'A' during letter shifting.

    import re

    # Step 1: Handle empty input
    if not encoded_sequence:
        return ""

    # Step 2: Split input based on given special characters
    groups = re.split(r'[@#$%^&*]', encoded_sequence)

    decoded_message = ""

    # Step 3: Process each group
    for group in groups:
        if not group:
            continue  # skip empty pieces from consecutive symbols

        # Check if group is binary (only 0s and 1s, and exactly 8 bits)
        if all(ch in '01' for ch in group) and len(group) == 8:
            # Convert binary to ASCII
            decimal_value = int(group, 2)
            decoded_message += chr(decimal_value)
        else:
            # Shift letters by +1 in the alphabet
            shifted_group = ""
            for ch in group:
                if ch == 'Z':
                    shifted_group += 'A'
                elif 'A' <= ch <= 'Y':
                    shifted_group += chr(ord(ch) + 1)
                else:
                    shifted_group += ch
            decoded_message += shifted_group

    # Step 4: Return the final decoded message
    return decoded_message
