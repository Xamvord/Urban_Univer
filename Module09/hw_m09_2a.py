def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            if y == 0:
                return "Error: Division by zero"
            else:
                return x / y
        return divide

func_add = create_operation("add")
print(func_add(12, 8))

func_subtract = create_operation("subtract")
print(func_subtract(100, 500))

func_multiply = create_operation(("multiply"))
print(func_multiply(6, 7))

func_divide = create_operation("divide")
print(func_divide(4, 2))
print(func_divide(4, 0))
