"""
Tongue Twister Competition Organizer
-----------------------------------

Challenge: Medium

Create a function named organize_tongue_twister_competition that receives
tongue_twisters, difficulty_levels, participants, and initial_scores as its parameters.

The function simulates a tongue-twisting competition at a local government office. 
It organizes the competition by pairing participants with tongue twisters based on 
their skills and the difficulty of the twisters, then calculates final scores.

Steps:
1. Sort tongue twisters based on difficulty (descending).
2. Pair participants (sorted by initial score) with tongue twisters.
3. Calculate final scores using: final_score = initial_score + (difficulty * 10).
4. Sort participants by final score (descending).
5. Return results as a 2D list: [participant_name, assigned_twister, final_score_as_string].

Validation:
- Ensure lengths of tongue_twisters == difficulty_levels
- Ensure lengths of participants == initial_scores
- There should be at least as many tongue twisters as participants.

Example:
----------
Input:
tongue_twisters = [
    "Peter Piper picked a peck of pickled peppers",
    "She sells seashells by the seashore",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "Red lorry, yellow lorry"
]
difficulty_levels = [8, 6, 7, 5]
participants = ["Alice", "Bob", "Charlie", "David"]
initial_scores = [75, 80, 70, 85]

Output:
[
    ['David', 'Peter Piper picked a peck of pickled peppers', '165'],
    ['Bob', 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?', '150'],
    ['Alice', 'She sells seashells by the seashore', '135'],
    ['Charlie', 'Red lorry, yellow lorry', '120']
]
"""

def organize_tongue_twister_competition(tongue_twisters, difficulty_levels, participants, initial_scores):
    """
    Organizes a tongue twister competition by assigning tongue twisters to participants
    based on their initial scores and the difficulty of the twisters, then calculates
    and ranks their final scores.

    Parameters:
    - tongue_twisters (list of str): The tongue twisters.
    - difficulty_levels (list of int): The corresponding difficulty of each twister.
    - participants (list of str): Participant names.
    - initial_scores (list of int): Initial scores of participants.

    Returns:
    - results (list of [str, str, str]): Each sublist contains [name, assigned_twister, final_score].
    """

    # Step 1: Pair tongue twisters with difficulty levels and sort by difficulty descending
    twisters = sorted(zip(tongue_twisters, difficulty_levels), key=lambda x: x[1], reverse=True)

    # Step 2: Pair participants with initial scores and sort by score descending
    players = sorted(zip(participants, initial_scores), key=lambda x: x[1], reverse=True)

    # Step 3: Assign tongue twisters to participants
    results = []
    for (name, init_score), (twister, diff) in zip(players, twisters):
        final_score = init_score + diff * 10
        results.append([name, twister, str(final_score)])

    # Step 4: Sort results by final score descending
    results.sort(key=lambda x: int(x[2]), reverse=True)
    return results


# Example usage (uncomment to test manually)
# tongue_twisters = [
#     "Peter Piper picked a peck of pickled peppers",
#     "She sells seashells by the seashore",
#     "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
#     "Red lorry, yellow lorry"
# ]
# difficulty_levels = [8, 6, 7, 5]
# participants = ["Alice", "Bob", "Charlie", "David"]
# initial_scores = [75, 80, 70, 85]
#
# print(organize_tongue_twister_competition(tongue_twisters, difficulty_levels, participants, initial_scores))
