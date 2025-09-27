# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.
    operation: 'add', 'subtract', 'multiply', 'divide'
    For division by zero, returns the string "Cannot divide by zero."
    """
    op = operation.strip().lower()
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        # unknown operation - return None so caller can detect
        return None
