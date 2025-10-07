def find_permutations(s: str) -> list:
    """
    Returns all possible permutations of a string in alphabetical order.

    Guidelines / Rules:
      - Input: a string `s` (may contain duplicate characters)
      - Output: list of all distinct permutations, sorted alphabetically
      - Use recursion or itertools.permutations
    """

    from itertools import permutations

    # Generate all possible permutations (tuples)
    perm_tuples = permutations(s)

    # Convert each tuple back to string
    perm_list = [''.join(p) for p in perm_tuples]

    # Remove duplicates (in case of repeated characters)
    unique_perms = sorted(set(perm_list))

    return unique_perms


# Example usage:
if __name__ == "__main__":
    print(find_permutations("abc"))
    # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
