# ======================================================
# Project: Exam Concentration Simulator
# Description:
# This project contains a function `exam_concentration_simulator`
# that simulates a student's thought process during an exam.
# It processes a list of questions according to their difficulty
# and specific conditions, demonstrating advanced string and
# list manipulations, control flow, and helper functions.
# ======================================================

def is_prime(n):
    """
    Helper function to check if a number is prime.
    
    Parameters:
    n (int): Number to check
    
    Returns:
    bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def exam_concentration_simulator(questions, difficulty_levels):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if len(questions) != len(difficulty_levels):
        raise ValueError("Questions and difficulty_levels must have the same length.")
    
    processed_questions = []

    for i in range(len(questions)):
        q = questions[i]
        diff = difficulty_levels[i]
        
        # Skip only if "explain" is lowercase
        if "explain" in q:
            continue
        
        if q.startswith("What") or q.startswith("How"):
            continue

        new_q = q

        if diff > 7:
            new_q = new_q[::-1]

        if is_prime(len(new_q)):
            new_q = ' '.join(new_q.split()[::-1])

        if diff % 3 == 0:
            new_q = ''.join(
                c.upper() if (idx+1) % 3 == 0 else c
                for idx, c in enumerate(new_q)
            )

        processed_questions.append(new_q)

    return processed_questions

# Test case
questions = ["Normal question here.", "EXPLAIN in all caps."]
difficulty_levels = [5, 5]
print(exam_concentration_simulator(questions, difficulty_levels))
# Output: ['Normal question here.', 'EXPLAIN in all caps.']

