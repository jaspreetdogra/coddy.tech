# ==============================================
# Project: Bill Split Calculator
# Difficulty: Beginner
# Source: Coddy.tech Mini Project
# ==============================================
#
# 📌 Project Overview:
# Did you know that splitting a bill with friends can be super easy 
# with a little bit of Python?
#
# In this project, you'll create a simple program that calculates how much 
# each person needs to pay, including the tip. It’s a practical way to apply 
# what you’ve learned about:
#   - Variables
#   - Arithmetic operations
#   - Basic input/output
#   - Type casting (float, int)
#   - f-strings formatting
#
# By the end of this lesson, you’ll have a handy tool 
# to use in real-life situations!
#
# ==============================================
# STEPS FROM LESSONS:
#
# 1. Welcome Message
#    - Every good program starts with a title/welcome line.
#
# 2. Getting Input
#    - Ask user for:
#        a) Bill amount (float)
#        b) Tip percentage (float)
#        c) Number of people splitting the bill (int)
#
# 3. Calculating Tip and Total
#    - tip_amount = (tip_percentage / 100) * bill_amount
#    - total_amount = bill_amount + tip_amount
#
# 4. Splitting the Bill
#    - per_person = total_amount / head_count
#
# 5. Formatted Output
#    - Print the title
#    - Print total and per person amount using f-strings
#    - Formatting style must exactly match:
#
# Example:
# Input:
#   100
#   5
#   2
#
# Output:
#   Bill Split Calculator
#   Total (including tip): $105.0
#   Each person pays: $52.5
#
# ==============================================
# FINAL IMPLEMENTATION:
# ==============================================

# Step 1: Welcome Message
print("Bill Split Calculator")

# Step 2: Inputs
bill_amount = float(input())      # First input: bill amount
tip_percentage = float(input())   # Second input: tip percentage
head_count = int(input())         # Third input: number of people

# Step 3: Calculate tip and total
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount

# Step 4: Split the bill
per_person = total_amount / head_count

# Step 5: Print formatted output
print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${per_person}")
