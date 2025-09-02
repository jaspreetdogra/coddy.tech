# Logical Operators Part 4
# -----------------------------------------------------------
# Lesson Recap:
# - not (A and B)  <=>  (not A) or (not B)
# - not (A or B)   <=>  (not A) and (not B)
#
# Example 1:
# number = 15
# result1 = not (number >= 1 and number <= 10)
# result2 = (not number >= 1) or (not number <= 10)
#
# Example 2:
# is_student = False
# is_employed = False
# result1 = not (is_student or is_employed)
# result2 = (not is_student) and (not is_employed)
#
# -----------------------------------------------------------
# Challenge (Beginner):
#
# You're helping a pet shop create a system to determine if they 
# can sell a pet to a customer.
#
# Step 1: Initialize variables
#   - has_license = True
#   - has_space = True
#   - has_experience = False
#
# Step 2: Logical expressions
#   - can_sell_regular_pet: Customer needs EITHER a license OR experience, AND must have space
#   - can_sell_exotic_pet: Customer needs BOTH a license AND experience, AND must have space
#   - cannot_sell_any_pet: Customer has NO license AND NO experience, OR has NO space
# -----------------------------------------------------------

# Initialize variables
has_license = True
has_space = True
has_experience = False

# Calculate conditions
can_sell_regular_pet = (has_license or has_experience) and has_space
can_sell_exotic_pet = has_license and has_experience and has_space
cannot_sell_any_pet = (not has_license and not has_experience) or (not has_space)

# Don't delete the lines below
print("Can sell regular pet:", can_sell_regular_pet)   # Expected: True
print("Can sell exotic pet:", can_sell_exotic_pet)     # Expected: False
print("Cannot sell any pet:", cannot_sell_any_pet)     # Expected: False
