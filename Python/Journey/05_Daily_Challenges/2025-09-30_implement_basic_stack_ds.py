"""
Daily Coding Challenge 🚀
-------------------------

📌 Challenge: Implement a Basic Stack Data Structure
Difficulty: Medium

📝 Description:
A Stack is a collection of elements that follows the **LIFO** principle (Last In, First Out).
That means the last element you add (push) will be the first one you take out (pop).

In this challenge, we implement a `Stack` class with:
1. `push(element)` → Adds an element to the stack
2. `pop()` → Removes and returns the most recently added element

⚠️ Constraints:
- The stack will only hold integers
- Popping from an empty stack should raise an error
- Adding a non-integer should raise a `TypeError`

🎯 Goal:
Write a working Stack class in Python that behaves like the standard stack data structure.
"""

# -----------------------------------------------------------
# ✅ Stack Implementation
# -----------------------------------------------------------

class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        Internally, we use a Python list to store stack elements.
        """
        self.items = []

    def push(self, element):
        """
        Add an element to the stack.
        Only integers are allowed.
        """
        if not isinstance(element, int):
            raise TypeError("❌ Stack only supports integers")
        self.items.append(element)

    def pop(self):
        """
        Remove and return the most recently added element.
        If the stack is empty, raise an IndexError.
        """
        if not self.items:
            raise IndexError("❌ Pop from empty stack")
        return self.items.pop()


# -----------------------------------------------------------
# ✅ Example Usage (Test Cases)
# -----------------------------------------------------------

if __name__ == "__main__":
    stack = Stack()

    # Pushing integers
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())  # Expected: 30
    print(stack.pop())  # Expected: 20
    print(stack.pop())  # Expected: 10

    # Uncomment below line to test popping from empty stack (will raise error)
    # print(stack.pop())
