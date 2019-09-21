countries = [
    "Canada",
    "China",
    "Mexico",
    "Japan",
    "Brazil",
    "Iran",
    "Korea",
    "Philippines",
    "USA"
]

print(countries[0]) # Canada
print(countries[-1]) # USA
print(countries[len(countries)-1]) # USA
print("*" * 40)

# Modify(change) elements - lists are mutable
print(countries)
countries[0] = "England"
print(countries)
print("*" * 40)

# Slicing lists (end index is not inclusive)
print(countries[0:3])
print("*" * 40)
countries[0:3] = ["Argentina", "Colombia", "Venezuela"]
print(countries)
print("*" * 40)
countries[0:3] = []
print(countries)
print("*" * 40)
# str vs list
# strings are immutable. (not mutable)
# lists are mutable. lists can have any type of elements
province = "AB"
# province[0] = "O"  # Does not support item assignment
print(province)

# re-assign a new valut to province
province = "ON"
print(province)
print("*" * 40)





