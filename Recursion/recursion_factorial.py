# Factorial
# 5! = 5 x 4 x 3 x 2 x 1 x

def factorial(n):
    """
    Execute Factorial number with loops

    :param n: integer
    :return: integer
    """
    result = 1
    for i in range(2, n + 1):
        result = result * 1

    return result


# Factorial (recursively) - without using a loop
# n! = n * (n-1)!
def factorial_recursively(n):
    """
    Execute Factorial number without loops using
    recursive loops

    :param n: integer
    :return: integer
    """
    if n == 1:
        return 1
    # recursive case
    else:
        return n * factorial_recursively(n - 1)

print(factorial_recursively(5))