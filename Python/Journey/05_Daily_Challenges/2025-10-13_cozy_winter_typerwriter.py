"""
Cozy Winter Typewriter Simulator
--------------------------------

Challenge: Medium

Create a function named `cozy_typewriter` that receives:
    - text (str): The text to be typed on the typewriter.
    - paper_width (int): The width of the paper (number of columns in the 2D array).
    - paper_height (int): The height of the paper (number of rows in the 2D array).
    - start_row (int): The starting row position of the typewriter.
    - start_col (int): The starting column position of the typewriter.

The function simulates typing text on an old typewriter onto a virtual sheet of paper represented
by a 2D array. As you type, the typewriter exhibits charming quirks that mimic old mechanical behavior.

--------------------------------------------------------------------------------
FEATURES TO IMPLEMENT
--------------------------------------------------------------------------------

1. Word Wrapping:
   - If a word doesn’t fit at the end of a line, move it to the next line.

2. Worn-Out Keys:
   - Some keys are worn and occasionally print similar-looking characters instead.
   - Replace characters based on their position in the text:
       • Every 7th 'o' → '0'
       • Every 5th 'l' → '1'
       • Every 6th 's' → '5'

3. Fading Ink:
   - As the typewriter continues typing, the ink fades:
       • After typing 30% of the total paper capacity → letters become lowercase.
       • After typing 60% of the total capacity → letters vanish (replaced by spaces).

4. Circular Paper:
   - The paper behaves circularly:
       • If the text reaches the bottom of the paper, continue from the top,
         overwriting existing text.

5. Carriage Return ('\\n'):
   - When a newline character is encountered, move to the beginning of the next line.

--------------------------------------------------------------------------------
RETURN VALUE
--------------------------------------------------------------------------------
- Returns a 2D list of characters representing the final paper after typing.

--------------------------------------------------------------------------------
EDGE CASES TO HANDLE
--------------------------------------------------------------------------------
- Empty input text.
- Paper dimensions too small to fit any text.
- Proper wrapping when encountering spaces or carriage returns.
--------------------------------------------------------------------------------

Example Usage:
---------------
paper = cozy_typewriter("Hello winter world", 10, 4, 0, 0)
for row in paper:
    print("".join(row))
"""

import re

def cozy_typewriter(text, paper_width, paper_height, start_row, start_col):
    # Initialize an empty paper filled with spaces
    paper = [[' ' for _ in range(paper_width)] for _ in range(paper_height)]
    
    # Initialize counters and position
    char_count = 0
    total_chars = paper_width * paper_height
    row, col = start_row, start_col
    o_count, l_count, s_count = 0, 0, 0

    # Preserve spaces and newlines (splitting with regex keeps '\n' and ' ' tokens)
    tokens = re.split(r'(\s+)', text)

    for token in tokens:
        if not token:
            continue

        # Handle explicit newline tokens
        if token == "\n":
            row = (row + 1) % paper_height
            col = 0
            continue

        # Handle multi-space/newline combos properly
        if token.isspace() and "\n" in token:
            for ch in token:
                if ch == "\n":
                    row = (row + 1) % paper_height
                    col = 0
                else:  # spaces
                    paper[row][col] = " "
                    col += 1
                    if col == paper_width:
                        row = (row + 1) % paper_height
                        col = 0
                    char_count += 1
            continue

        # Word wrapping: move to next line if word doesn't fit
        if col + len(token) > paper_width:
            row = (row + 1) % paper_height
            col = 0

        # Type each character of the word
        for char in token:
            if char == "\n":
                row = (row + 1) % paper_height
                col = 0
                continue

            # Worn-out keys logic
            if char.lower() == 'o':
                o_count += 1
                if o_count % 7 == 0:
                    char = '0'
            elif char.lower() == 'l':
                l_count += 1
                if l_count % 5 == 0:
                    char = '1'
            elif char.lower() == 's':
                s_count += 1
                if s_count % 6 == 0:
                    char = '5'

            # Fading ink logic
            if char_count > 0.6 * total_chars:
                char = ' '
            elif char_count > 0.3 * total_chars:
                char = char.lower()

            # Place character on paper
            paper[row][col] = char
            col += 1
            if col == paper_width:
                row = (row + 1) % paper_height
                col = 0

            char_count += 1

    return paper


# -------------------------------------------------------------------------
# Example Run (for GitHub ReadMe preview)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    demo_text = "Circular paper test with carriage return\nNew line here"
    paper = cozy_typewriter(demo_text, 15, 4, 2, 2)
    for row in paper:
        print("".join(row))
