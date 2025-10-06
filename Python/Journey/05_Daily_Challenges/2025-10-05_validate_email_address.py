def is_valid_email(email: str) -> bool:
    """
    Validates an email address according to the rules used in the challenge.

    Rules enforced:
      - Exactly one '@' separating local (username) and domain parts.
      - Username may contain letters, digits, '.', '-', '_' .
      - Username must not start or end with '.' (leading/trailing '.' invalid).
      - Domain must contain at least one '.' (dot).
      - The part before the last dot (domain name) may contain letters, digits, and '-' only.
      - The domain name must not start or end with '-' (leading/trailing '-' invalid).
      - The extension (after the last dot) must consist of letters only (e.g. 'com', 'org').
    """

    # must contain exactly one '@'
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    # username must be non-empty
    if not username:
        return False

    # allowed chars in username: letters, digits, '.', '-', '_'
    for ch in username:
        if not (ch.isalnum() or ch in {".", "-", "_"}):
            return False

    # username cannot start or end with a dot
    if username[0] == "." or username[-1] == ".":
        return False

    # domain must contain a dot and must not start or end with a dot
    if "." not in domain or domain[0] == "." or domain[-1] == ".":
        return False

    # split domain into domain_name and extension using last dot
    domain_name, extension = domain.rsplit(".", 1)

    # domain_name must be non-empty
    if not domain_name:
        return False

    # domain_name may contain letters, digits, and hyphen
    for ch in domain_name:
        if not (ch.isalnum() or ch == "-"):
            return False

    # domain_name must not start or end with a hyphen
    if domain_name[0] == "-" or domain_name[-1] == "-":
        return False

    # extension must be letters only and at least one character
    if not extension or not extension.isalpha():
        return False

    return True


# Quick manual tests (uncomment to run)
if __name__ == "__main__":
    tests = [
        ("j.doe@example.com", True),
        ("johndoe123@gmail.com", True),
        ("j-doe_456@example-mail.com", True),
        ("johndoe", False),
        ("johndoe@", False),
        ("@example.com", False),
        ("johndoe@.com", False),
        ("johndoe@example.", False),
        ("johndoe@example.com-", False),
        ("-johndoe@example.com", True),
    ]

    for email, expected in tests:
        out = is_valid_email(email)
        print(f"{email:30} -> {out} (expected: {expected})")
