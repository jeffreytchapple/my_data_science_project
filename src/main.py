def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b

def add_10(a):
    if not isinstance(a, (int, float)):
        raise ValueError("Argument must be a number.")
    return add(a, 10)

def square(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Argument must be a number.")
    return x * x