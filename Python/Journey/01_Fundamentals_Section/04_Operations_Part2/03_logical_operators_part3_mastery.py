# Logical Operator 3 Mastery
# -----------------------------------------------------------
# Challenge (Easy)
#
# You're helping a weather app determine suitable outdoor activities 
# based on weather conditions. 
#
# Task:
# Create a program that uses logical operations to determine if 
# certain activities are possible.
#
# Step 1: Initialize the following variables:
#   - is_sunny = True
#   - temperature = 25
#   - wind_speed = 10
#   - water_temperature = 22
#
# Step 2: Write the following logical expressions:
#   - can_go_hiking: It's sunny AND temperature > 15°C AND wind speed < 20 km/h
#   - can_go_swimming: It's sunny AND temperature > 20°C AND water temperature > 18°C
#   - cannot_go_outside: It's NOT sunny OR temperature < 10°C OR wind speed > 30 km/h
#
# Step 3: Print the results clearly.
# -----------------------------------------------------------

# Initialize variables
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Calculate conditions
can_go_hiking = is_sunny and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temperature > 20 and water_temperature > 18
cannot_go_outside = (not is_sunny) or temperature < 10 or wind_speed > 30

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)        # Expected: True
print("Can go swimming:", can_go_swimming)    # Expected: True
print("Cannot go outside:", cannot_go_outside)  # Expected: False
