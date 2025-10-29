# -----------------------------------------------------------
# Challenge: Mathematical Library Organizer
# Difficulty: Hard
#
# Guided Material / Instructions:
#
# Task:
#   Create a function named `organize_math_library` that simulates a librarian
#   organizing mathematical reference books for students.
#
# Parameters:
#   - library_sections (list of lists of str): 
#       Each inner list represents a section containing strings about
#       mathematical constants or operations.
#   - num_students (int): 
#       The number of students who will receive a summarized version of results.
#
# Steps to Implement:
#
#   Step 1: Parse the input `library_sections`
#       - Identify constants: e, pi, phi
#       - Identify operations: sin, cos, tan, log
#       - Store them in separate lists for further use.
#
#   Step 2: Create a dictionary of constants with precise values:
#       e   = 2.7182818284
#       pi  = 3.1415926535
#       phi = 1.6180339887
#
#   Step 3: Define lambda functions for mathematical operations:
#       sin(x), cos(x), tan(x), log(x)
#
#   Step 4: Perform calculations:
#       - For each constant, apply all operations (sin, cos, tan, log)
#       - Store results in a 2D list named `books`
#       - Compute GCD of the floor values of every pair of constants
#         and add those results to `books` as well.
#
#   Step 5: Data Processing using map, filter, reduce
#       - Map: Format all floats to 6 decimal places.
#       - Filter: Remove 'inf' or 'NaN' results.
#       - Reduce: Concatenate all valid results into a single comma-separated string.
#
#   Step 6: Distribute processed results among students
#       - Divide processed results equally among all students.
#       - Store each student’s summary as "Student X": summary_string
#
# Return:
#   - A dictionary mapping each student to their processed string summary.
#
# Example:
#   Input:
#       library_sections = [["e", "pi", "phi"], ["sin", "cos", "tan", "log"]]
#       num_students = 2
#   Output:
#       {
#           "Student 1": "0.410781, -0.989993, -1.557408, 1.000000, 0.841471, -0.540302, -0.142547, 1.000000",
#           "Student 2": "1.000000, 1.000000, 1.000000"
#       }
# -----------------------------------------------------------

import math
from functools import reduce

def organize_math_library(library_sections, num_students):
    # Step 1: Parse library_sections to separate constants and operations
    constants = []
    operations = []
    for section in library_sections:
        for item in section:
            if item in ['e', 'pi', 'phi']:
                constants.append(item)
            elif item in ['sin', 'cos', 'tan', 'log']:
                operations.append(item)
    
    # Step 2: Dictionary of constants with their numeric values
    constant_values = {
        'e': 2.7182818284,
        'pi': 3.1415926535,
        'phi': 1.6180339887
    }
    
    # Step 3: Lambda functions for mathematical operations
    op_functions = {
        'sin': lambda x: math.sin(x),
        'cos': lambda x: math.cos(x),
        'tan': lambda x: math.tan(x),
        'log': lambda x: math.log(x)
    }
    
    # Step 4: Perform calculations for each constant
    books = []
    for const in constants:
        book = []
        for op in ['sin', 'cos', 'tan', 'log']:
            book.append(op_functions[op](constant_values[const]))
        books.append(book)
    
    # Step 4.1: Calculate GCDs between floor values of each constant pair
    const_pairs = [(constants[i], constants[j]) for i in range(len(constants)) for j in range(i+1, len(constants))]
    for pair in const_pairs:
        gcd = math.gcd(int(constant_values[pair[0]]), int(constant_values[pair[1]]))
        books.append([float(gcd)])
    
    # Step 5: Process results using map, filter, and reduce
    def map_function(x):
        return f"{x:.6f}"
    
    def filter_function(x):
        return not (math.isinf(float(x)) or math.isnan(float(x)))
    
    def reduce_function(acc, x):
        return acc + ", " + x if acc else x
    
    processed_books = []
    for book in books:
        mapped = list(map(map_function, book))
        filtered = list(filter(filter_function, mapped))
        reduced = reduce(reduce_function, filtered, "")
        processed_books.append(reduced)
    
    # Step 6: Divide results among students evenly
    summaries = {}
    for i in range(num_students):
        start = i * (len(processed_books) // num_students)
        end = (i + 1) * (len(processed_books) // num_students)
        summary = ", ".join(processed_books[start:end])
        summaries[f"Student {i+1}"] = summary
    
    return summaries


# ---------------- Example Run ----------------
library_sections = [["e", "pi", "phi"], ["sin", "cos", "tan", "log"]]
print(organize_math_library(library_sections, 2))
