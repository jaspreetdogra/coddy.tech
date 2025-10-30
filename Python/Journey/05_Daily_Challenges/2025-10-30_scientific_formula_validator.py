import re
import math

def validate_scientific_formula(formula):
    """
    Validates a given scientific formula string and returns diagnostic information.
    Checks syntax, structure, notation, dimensionality, and complexity.
    """

    # --- Initialize result container ---
    result = {
        'is_valid': True,
        'errors': [],
        'suggestions': [],
        'complexity_score': 0
    }

    # --------------------------------------------------------
    # Helper function 1: Check for balanced parentheses
    # --------------------------------------------------------
    def check_balanced_parentheses(s):
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if not stack or pairs[stack.pop()] != char:
                    return False
        return len(stack) == 0

    # --------------------------------------------------------
    # Helper function 2: Detect scientific notation (e.g., 1.23e+4)
    # --------------------------------------------------------
    def has_scientific_notation(s):
        pattern = r'\d+\.?\d*[eE][+-]?\d+'
        return bool(re.search(pattern, s))

    # --------------------------------------------------------
    # Helper function 3: Check for physical units (for dimensional analysis)
    # --------------------------------------------------------
    def has_units(s):
        units = ['m', 's', 'kg', 'A', 'K', 'mol', 'cd']
        return bool(re.search(r'\b(' + '|'.join(units) + r')\b', s))

    # --------------------------------------------------------
    # Step 1: Check for balanced parentheses
    # --------------------------------------------------------
    if not check_balanced_parentheses(formula):
        result['is_valid'] = False
        result['errors'].append("Unbalanced parentheses found in formula.")

    # --------------------------------------------------------
    # Step 2: Validate operators and functions
    # --------------------------------------------------------
    valid_operators = {'+', '-', '*', '/', '^', '='}
    valid_functions = {'sin', 'cos', 'tan', 'log', 'ln', 'exp', 'sqrt'}

    # Find used operators and functions
    used_operators = set(re.findall(r'[+\-*/^=]', formula))
    used_functions = set(re.findall(r'\b(sin|cos|tan|log|ln|exp|sqrt)\b', formula))

    # Detect invalid ones
    invalid_ops = used_operators - valid_operators
    invalid_funcs = used_functions - valid_functions

    if invalid_ops:
        result['is_valid'] = False
        result['errors'].append(f"Invalid operators found: {', '.join(invalid_ops)}")

    if invalid_funcs:
        result['is_valid'] = False
        result['errors'].append(f"Invalid functions found: {', '.join(invalid_funcs)}")

    # --------------------------------------------------------
    # Step 3: Check for scientific notation
    # --------------------------------------------------------
    if has_scientific_notation(formula):
        result['complexity_score'] += 1
    else:
        result['suggestions'].append("Use scientific notation (e.g., 1.23e+4) for large/small numbers.")

    # --------------------------------------------------------
    # Step 4: Check dimensional analysis (presence of units)
    # --------------------------------------------------------
    if has_units(formula):
        result['complexity_score'] += 1
    else:
        result['suggestions'].append("Add units (m, s, kg, etc.) to ensure dimensional consistency.")

    # --------------------------------------------------------
    # Step 5: Check for advanced math operations (LaTeX-like)
    # --------------------------------------------------------
    if '\\int' in formula:  # Integral
        result['complexity_score'] += 2
    if '\\frac' in formula:  # Fraction
        result['complexity_score'] += 1
    if '\\sum' in formula or '\\prod' in formula:  # Summation/Product
        result['complexity_score'] += 2

    # --------------------------------------------------------
    # Step 6: Check for Greek letters
    # --------------------------------------------------------
    greek_letters = [
        'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta',
        'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron',
        'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'
    ]

    greek_found = [g for g in greek_letters if g in formula.lower()]

    if greek_found:
        result['complexity_score'] += len(greek_found)
    else:
        result['suggestions'].append("Include Greek letters (e.g., alpha, beta, pi) if relevant to variables/constants.")

    # --------------------------------------------------------
    # Step 7: Final complexity adjustment
    # --------------------------------------------------------
    result['complexity_score'] = min(result['complexity_score'], 10)

    return result
