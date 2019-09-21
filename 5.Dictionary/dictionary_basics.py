# lists, strings, tuples: index-based (0,1,2,3 ...)
# Dictionary: A collection of a key-value pairs
# A dictionary is similar to a list, except that you access its values by looking up
# a key instead of an index. A key can be any string or a number
contacts = {
    "John": "778-123-1234",
    "Dan":  "604-842-1234",
    "Max":  "778-123-9872"
    # "John": "604-123-5678",  # Don't repeat a key
}

print(contacts["John"])
print("*" * 40)

contacts["Silva"] = "780-123-4783" # add a new item to te dictionary
print(contacts)
contacts["Silva"] = "604-123-8548" # add a new item to te dictionary
print(contacts)
print("*" * 40)
del contacts["John"]  # remove key-value pair from the dictionary
print(contacts)
print("*" * 40)
# Get the keys
print(contacts.keys())
print(list(contacts.keys()))
print("*" * 40)
print(contacts.values())
print(list(contacts.values()))
print("*" * 40)
# 'in' keyword
# The in keyword is used to check if a list or dictionary
# contains a specific item
print("John" in contacts)
print("*" * 40)

