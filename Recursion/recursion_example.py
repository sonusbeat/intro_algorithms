# prints the given number of stars in the console
# assume n >= 1

def print_stars(n):
    if n == 1:  # base case
        print("*", end="")
    else:  # recursive case
        print("*", end="")
        print_stars(n-1)


print_stars(1)
print()
print_stars(3)
print()
print_stars(5)
