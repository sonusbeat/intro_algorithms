# Functions are a convenient way to divide your code into
# useful block, make it more readable and help 'reuse' it.
# In Python, functions are defined using the keyword
# 'def', followed by funtion's name.

# "A reusable block of code"

# Define a function
def print_menu():
    print("MENU")
    print("1. Tacos")
    print("2. Brazilian BBQ")
    print("3. Kebab")
    print("4. Hotpot")
    print("5. Sashimi")
    print("6. Sinigang")
    print("7. Kimchi")


# Run, run, execute the function
# for _ in range(2):
#     print_menu()

# Parameters vs Arguments
def add_two(a, b):
    return a + b

result = add_two(10, 20)  # 10, 20: arguments
print(result)
print("#" * 30)

# Exercise: define a function similar to 'range' function.
# Default parameters
def my_range(start, end=0, steps=1):
    """"
    Returns a list of integers from start to end by steps
    :param start: start number
    :param end: end number
    :return a list of integers
    """
    alist = []
    s = start
    while s < end:
        alist.append(s)
        s += steps
    return alist

print(my_range(1, 10, 2))
print(my_range(1, 20))
print("#" * 30)

def your_range(*args):
    if len(args) == 1:
        alist = []
        i = 0
        while i < args[0]:
            alist.append(i)
            i += 1
        return alist
    elif len(args) == 2:
        return my_range(args[0], args[1])
    elif len(args) == 3:
        return my_range(args[0], args[1], args[2])
    else:
        print("Invalid number of arguments.")
        return []


print(your_range(10))
print(your_range(1, 10))
print(your_range(1, 10, 2))