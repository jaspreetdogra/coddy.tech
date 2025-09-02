# Logical Operators Part 4 - Mastery Challenge
# -----------------------------------------------------------
# Context:
# In this lesson, we learned how logical operators can be 
# combined and simplified:
#   - not (A and B)  <=>  (not A) or (not B)
#   - not (A or B)   <=>  (not A) and (not B)
#
# Now, let’s apply this knowledge to a practical scenario.
#
# -----------------------------------------------------------
# Challenge (Easy):
#
# You're helping a transportation company create a system to 
# determine if a person can drive certain vehicles.
#
# Step 1: Initialize variables
#   - has_license = True
#   - has_experience = False
#   - has_clean_record = True
#
# Step 2: Logical expressions
#   - can_drive_car: Person needs a license AND a clean record
#   - can_drive_truck: Person needs a license AND experience AND a clean record
#   - cannot_drive_any: Person has NO license OR NO clean record
# -----------------------------------------------------------

# Initialize variables
has_license = True
has_experience = False
has_clean_record = True

# Calculate conditions
can_drive_car = has_license and has_clean_record
can_drive_truck = has_license and has_experience and has_clean_record
cannot_drive_any = (not has_license) or (not has_clean_record)

# Don't delete the lines below
print("Can drive car:", can_drive_car)       # Expected: True
print("Can drive truck:", can_drive_truck)   # Expected: False
print("Cannot drive any:", cannot_drive_any) # Expected: False
