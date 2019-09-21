# 'in' operator
# If you want to check whether a string contains a specific letter or
# a substring, you can use 'in' keyword.
favorite = "ice cream" " " "helado"
print(favorite)
print("ice" in favorite)  # Prints boolean result directly
print('*' * 40)
# Escaping characters (\", \')
dont_worry = "Don't worry about the \"weather\" !"
print(dont_worry)
print('*' * 40)
message = "Hi,\nHow are you?\nI'm doing good!"
print(message)
print('*' * 40)
# Multi-line strings
phrase = """It is a really long string
tripple-quoted strings are used
to define multi-line strings"""
print(phrase)
print('*' * 40)

# String formatting
name = 'Daniel'
message = "Hello, Pycharm! My name is %s" % name
print(message)
print('*' * 40)
current_year = 2019
year = "Current year is: %d" % current_year
print(year)
print('*' * 40)
info = "name = %s, year = %d" % (name, current_year)
print(info)
print('*' * 40)

# String interpolation (from python 3.6)
a = 3
b = 4
print(f"{a} x {b} = {a * b}")
