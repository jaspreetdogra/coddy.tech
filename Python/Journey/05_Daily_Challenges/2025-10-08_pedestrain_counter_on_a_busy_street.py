# Function: count_pedestrians
# Purpose:
#   Simulates counting pedestrians on a busy street using both
#   'break' and 'continue' statements, and also includes
#   string reversal for the elderly count.
#
# Parameters:
#   pedestrian_sequence (str): A string representing pedestrians where:
#       'A' -> Adult
#       'C' -> Child
#       'E' -> Elderly
#       'X' -> Stop sign
#   max_count (int): The maximum number of pedestrians to count before stopping.
#
# Rules:
#   1. Skip children ('C') using a 'continue' statement.
#   2. Stop counting if:
#         - A stop sign ('X') is encountered (reason: "Stop sign")
#         - Maximum count (max_count) is reached (reason: "Max reached")
#   3. Reverse the count of elderly pedestrians before returning.
#
# Returns:
#   A string in the format:
#       "adults_count,reversed_elderly_count,reason"

def count_pedestrians(pedestrian_sequence, max_count):
    # Initialize counters
    adult_count = 0
    elderly_count = 0
    total_count = 0
    reason = ""

    # Iterate through each pedestrian in the sequence
    for p in pedestrian_sequence:
        # Skip children using 'continue'
        if p == 'C':
            continue

        # If a stop sign is encountered, break the loop
        if p == 'X':
            reason = "Stop sign"
            break

        # Count adults and elderly pedestrians
        if p == 'A':
            adult_count += 1
        elif p == 'E':
            elderly_count += 1

        # Increase total pedestrians counted
        total_count += 1

        # If maximum count reached, stop counting
        if total_count >= max_count:
            reason = "Max reached"
            break

    # If loop finishes naturally without a stop sign or break,
    # and we have not reached max count, we still consider it as max reached
    if reason == "":
        reason = "Max reached"

    # Reverse the elderly count (as a string)
    reversed_elderly = str(elderly_count)[::-1]

    # Prepare the final result string
    result = f"{adult_count},{reversed_elderly},{reason}"

    return result


# -------------------- SAMPLE TESTS --------------------

# Test Case 1:
# Sequence includes adults, children, and elderly. Stops naturally after max reached.
print(count_pedestrians("EEAAACCCAA", 10))
# Expected Output: "5,2,Max reached"

# Test Case 2:
# Stop sign encountered before max reached.
print(count_pedestrians("AAECAEXA", 5))
# Expected Output: "2,1,Max reached"

# Test Case 3:
# Stops because of a stop sign.
print(count_pedestrians("AACEXAEA", 10))
# Expected Output: "2,1,Stop sign"

# Test Case 4:
# Only elderly, less than max count, no stop sign.
print(count_pedestrians("EEEE", 10))
# Expected Output: "0,4,Max reached"
