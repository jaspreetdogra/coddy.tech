def check_password_strength(password: str) -> str:
    """
    Checks the strength of a password based on five criteria:
      1. At least 8 characters long
      2. Contains at least one uppercase letter (A-Z)
      3. Contains at least one lowercase letter (a-z)
      4. Contains at least one digit (0-9)
      5. Contains at least one special character (!@#$ etc.)
    
    Returns:
      "Weak"     -> if fewer than 3 criteria met
      "Moderate" -> if 3 or 4 criteria met
      "Strong"   -> if all 5 criteria met
    """

    # Initialize count for satisfied criteria
    criteria_met = 0

    # 1️⃣ Length check
    if len(password) >= 8:
        criteria_met += 1

    # 2️⃣ Uppercase letter check
    if any(ch.isupper() for ch in password):
        criteria_met += 1

    # 3️⃣ Lowercase letter check
    if any(ch.islower() for ch in password):
        criteria_met += 1

    # 4️⃣ Digit check
    if any(ch.isdigit() for ch in password):
        criteria_met += 1

    # 5️⃣ Special character check (not alphanumeric)
    if any(not ch.isalnum() for ch in password):
        criteria_met += 1

    # Return based on criteria count
    if criteria_met < 3:
        return "Weak"
    elif criteria_met < 5:
        return "Moderate"
    else:
        return "Strong"


# Example test cases
if __name__ == "__main__":
    print(check_password_strength("abc"))              # Weak
    print(check_password_strength("Abcdef12"))         # Moderate
    print(check_password_strength("Abc@1234"))         # Strong
    print(check_password_strength("password"))          # Weak
    print(check_password_strength("Pass12"))           # Weak
