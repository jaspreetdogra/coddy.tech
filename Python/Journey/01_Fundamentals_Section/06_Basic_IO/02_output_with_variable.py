# Output With Variables in Python

# Theory:
# We have learned how to print simple strings, but to include variable values inside a string,
# we use f-strings.
# Example:

age = 10
print("His age is: age")  # Will print: His age is: age

# Correct way using f-string:
print(f"His age is: {age}")  # Will print: His age is: 10

# Quiz:
# What is the purpose of using f before the quotation marks in Python strings?
# 1) To indicate the string should be read from a file
# 2) To make the string formatted, allowing variables to be inserted within the string  <- Correct
# 3) To format the string as fixed-width
# 4) To flag the string as 'fast' and optimize its storage

# Challenge:
# Given a variable rnd containing input, print it in a sentence
rnd = input()  # Don't change this line
print(f"The input is: {rnd}")
