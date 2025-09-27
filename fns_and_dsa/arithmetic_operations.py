def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.
    operation: 'add', 'subtract', 'multiply', 'divide'
    Returns numeric result (float) for math operations.
    If division by zero requested, returns the exact string:
        "Cannot divide by zero."
    Unknown operation -> returns None
    """
    operation = str(operation).strip().lower()

    if operation == "add":
        return float(num1) + float(num2)
    elif operation == "subtract":
        return float(num1) - float(num2)
    elif operation == "multiply":
        return float(num1) * float(num2)
    elif operation == "divide":
        if float(num2) == 0.0:
            return "Cannot divide by zero."
        return float(num1) / float(num2)
    else:
        return None
