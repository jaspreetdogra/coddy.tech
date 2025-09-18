"""
Daily Challenge: Is the Number Even or Odd?

📌 Challenge:
Write a program that gets a number as input and outputs "even" if the number is even,
otherwise "odd".

🎯 Learning Goal:
- Practice basic input/output in Python
- Use conditional statements (if-else)
- Understand the modulo (%) operator

✅ Expected Behavior:
Input: 4   → Output: even
Input: 7   → Output: odd
"""

def main():
    # Step 1: Take user input and convert it to integer
    number = int(input())

    # Step 2: Check if the number is divisible by 2
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Standard Python entry point
if __name__ == "__main__":
    main()
