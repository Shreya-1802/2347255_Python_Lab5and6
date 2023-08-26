def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

numerator = 10
denominator = 0
result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"Result: {result}")
