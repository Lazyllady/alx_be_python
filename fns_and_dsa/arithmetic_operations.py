def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.
    operation: 'add', 'subtract', 'multiply', 'divide'
    Returns float result, or the exact string
    "Cannot divide by zero." when dividing by zero.
    """
    # ensure numeric types
    num1 = float(num1)
    num2 = float(num2)

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            # explicit divide-by-zero handling
            return "Cannot divide by zero."
        return num1 / num2
    else:
        # unrecognised operation
        return None

