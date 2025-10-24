# Challenge: Return the Middle Character of a String
# Difficulty: Easy
#
# 🧭 Guided Material / What to Do:
# Write a function named get_middle_char(s) that takes a string s as input 
# and returns the middle character(s) of the string, or an empty string 
# if the length of the input string is even.
#
# 🧠 Steps to Solve:
# 1️⃣ Find the length of the string using len(s).
# 2️⃣ If the string’s length is even, return an empty string "".
# 3️⃣ If the string’s length is odd:
#      - Find the middle index: len(s) // 2
#      - Return the character at that position.
#
# 🧮 Parameters:
# - s (str): The input string from which the middle character(s) will be extracted.
#
# 🏁 Return:
# - str: The middle character if the length is odd, 
#        or an empty string if the length is even.
#
# 🧪 Example:
# get_middle_char("hello") ➜ "l"
# get_middle_char("test") ➜ ""

def get_middle_char(s):
    # Get the length of the input string
    length = len(s)
    
    # If the length is even, return an empty string
    if length % 2 == 0:
        return ""
    
    # Otherwise, return the middle character
    middle_index = length // 2
    return s[middle_index]


# 🧪 Example Tests:
print(get_middle_char("hello"))  # Expected Output: "l"
print(get_middle_char("test"))   # Expected Output: ""
print(get_middle_char("a"))      # Expected Output: "a"
print(get_middle_char("abcde"))  # Expected Output: "c"
