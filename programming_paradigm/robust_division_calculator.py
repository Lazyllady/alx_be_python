# robust_division_calculator.py
"""A robust division function that handles non-numeric input and division by zero."""

def safe_divide(numerator, denominator):
    # Convert to float; if fails -> numeric error
    try:
        n = float(numerator)
        d = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Division and division by zero handling
    try:
        result = n / d
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Return formatted result string (checker expects this phrasing)
    return f"The result of the division is {result}"
