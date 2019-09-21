# Data structure
# list: A sequence of items (elements)

# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]

print(squares)

# 2. indexlist operations
animals = ["Eagle", "Snake", "Panda", "Lion", "Tiger", "Bear"]
print(animals)
animals += ["Koala", "Dog"]  # add two items to the end of the list
print(animals)

animals.append("Cat")  # add "Cat" item to the end of the list
print(animals)
animals.insert(0, "Monkey")  # insert "Monkey" at 0 index
print(animals)

animals.remove("Monkey")  # remove item "Monkey"
print(animals)

# remove the element at index 0
# and returns the item
print(animals.pop(0))

print(animals.count("Cat"))  # 1
print("*" * 40)
print(animals.index("Panda"))  # 1

