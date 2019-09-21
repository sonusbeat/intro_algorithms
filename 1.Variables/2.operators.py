# Operators
# + addition
# - addition
# / float division
# // int division
# % (modulo) division
# ** (power)

print(10 % 3)  # 1
print(10 ** 2)  # 100

# = assignment operator
number = 7
number = number + 3  # 10

print("number = " + str(number))

# += increment operator
number += 3
print("number = " + str(number))

# -= decrement operator
number -= 3
print("number = " + str(number))

# *= multiply operator
number *= 3
print("number = " + str(number))

# *= divide operator
number /= 3
print("number = " + str(number))

# Boolean operators
# Boolean (bool) is a type of value that can only be True or False.

# Comparison
# ==: equality (equal)
print(3 == 4) # false
# > : greater than and equal to
# >= : greater than or equal to
# < : less than
# <= : less than or equal to
print(3 < 4)

# This chained comparison means that the (3 < 4) and (4 < 5)
# comparisons are performed at the same time
print(3 < 4 < 5)
print((3 < 4) and (4 < 5))
print((3 != 4) or (4 == 5)) # either one fo them is True => True

# Exercise
num = 10
# print(num / 0)
# print((num > 1) and (num / 0 == 0)) # Error
print((num > 10) and (num / 0 == 0))  # False
print((num > 1) or (num / 0 == 0))  # True
print((num > 10) or (num / 0 == 0))  # True
print(not true)  # False
print(not false)  # True
