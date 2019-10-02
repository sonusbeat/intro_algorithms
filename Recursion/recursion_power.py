# consider the following function to compute exponents
# returns base^exp
# precondition: exponent >= 0

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result

print("Loop Way")
print(power(2, 10))
print(power(5, 3))
print("*" * 40)
def power_recursive(base, exponent):
    if base == 0: # base
        return 1

    # recursive
    return power_recursive(base, exponent-1)


print("Recursive Way")
print(power(2, 10))
print(power(5, 3))

print("*" * 40)