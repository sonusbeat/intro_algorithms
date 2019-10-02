# Fibonacci Sequence
# fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
#           position: 0, 1, 2, 3, 4, 5,  6,  7,  8,  9, 10 ...

# Examples
# fibonacci(1)
# fibonacci(2)
# fibonacci(6)
# fibonacci(10)
# fibonacci(1)
# fibonacci(1)

def fibonacci(n):
    """ Iteratively (loop) """
    a = 1
    b = 1
    # c = a + b
    # d = b + c
    # e = c + d

    for _ in range(n-1):  # a, b (we already have 2 numbers)
        a, b = b, a + b

    return a


print(fibonacci(6))
print(fibonacci(10))

# fib(n) = fib(n-1) + fib(n -2)
# factorial(n) = n * factorial (n -1)

def fibonacci_recursive(n):
    """ Recursively (no loop) """
    # base
    if n == 0 or n == 1:
        return 1
    # recursive
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

