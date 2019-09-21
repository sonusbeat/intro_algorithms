# Tuples are almost identical to lists.
# The only big difference between lists and tuples is that
# tuples cannot be modified (immutable).
# You cannot add(append), change, or delete elements from the tuple.

# Tuples = 'immutable lists'
vowel_alphabets = ("a", "e", "i", "o", "u")

# vowel_alphabets[0] = "k"  # Error
# print(vowel_alphabets)

# "syntactic sugar" - 1_000_000
print(1_000_000)
print("*" * 40)

# Use cases
# 1. return multiple values from a function
a = (1_000_000 * 1_000, "Daniel")

# 2. check if an item is in a collection
print("a" in vowel_alphabets)
print("*" * 40)

# 3. multiple assignments
year, country = (2019, "Canada")

print(year)
print(country)
print(vowel_alphabets[0])