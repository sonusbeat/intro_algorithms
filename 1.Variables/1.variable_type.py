# Data types
# There are many different data types in Python
# int: integer
# float: floatin poin (2.2, 5.98, 7.12)
# str: a sequence of chars in quotes "aa", 'bb'

language = "en_us"

print(type(language))

users = 10
# print(users + language)

# Type conversion (type casting): changing types
# There are several built-in functions that let you convert
# one data type to another.
# int(x): x to an integer.
# float(x): converts x to a floating-point number.
# str(x): converts x to a string representation

print(str(users) + language)  # "10 + "en_us" -> "10en_us"

# Exercise: What is the type of the following operations ?
# 1. 10 / 2
print(type(10 / 2))  # / : float division 5.0

# 2. 10 // 2
print(type(10 // 2))  # // : int division 5

# 3. float(5)
print(float(5))  # / 5.0
