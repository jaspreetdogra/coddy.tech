# Challenge: Alphabet Soup
# Difficulty: Easy
#
# 🧭 Guided Material / What to Do:
# Write a function named alphabet_soup that accepts a string 
# and returns it with its letters arranged in alphabetical order.
#
# 🧠 Steps to Solve:
# 1️⃣ Take the input string.
# 2️⃣ Convert it into a list of characters using list() or simply iterate over it.
# 3️⃣ Sort the characters alphabetically using Python’s built-in sorted() function.
# 4️⃣ Join the sorted characters back into a single string using ''.join().
# 5️⃣ Return the new alphabetically sorted string.
#
# 🧮 Parameters:
# - s (str): The input string containing letters.
#
# 🏁 Return:
# - str: The alphabetically sorted version of the input string.
#
# 🧪 Examples:
# alphabet_soup("hello") ➜ "ehllo"
# alphabet_soup("coddy") ➜ "cddoy"
# alphabet_soup("hacker") ➜ "acehkr"

def alphabet_soup(s):
    # Sort the characters in the string alphabetically and return the result
    return ''.join(sorted(s))


# 🧪 Example Tests:
print(alphabet_soup("hello"))   # Expected Output: "ehllo"
print(alphabet_soup("coddy"))   # Expected Output: "cddoy"
print(alphabet_soup("hacker"))  # Expected Output: "acehkr"
print(alphabet_soup("python"))  # Expected Output: "hnopty"