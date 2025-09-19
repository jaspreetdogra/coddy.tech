"""
Challenge: Remove Repeated Characters from a String

Easy

Write a function remove_repeated_chars(s) that takes a string s as input 
and returns a new string with repeated characters removed.

Example:
-----------
Input:  "programming"
Output: "progamin"

Input:  "mississippi"
Output: "misp"
"""

def remove_repeated_chars(s: str) -> str:
    result = ""
    seen = set()
    
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result


# Example runs
if __name__ == "__main__":
    print(remove_repeated_chars("programming"))  # Expected: "progamin"
    print(remove_repeated_chars("mississippi"))  # Expected: "misp"
