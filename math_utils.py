# math_utils.py

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
