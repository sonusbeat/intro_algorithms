city = "vancouver"
print(city.upper())
print("*" * 40)
print(city.capitalize())
print("*" * 40)
print("VANCOUVER".lower())
print("*" * 40)
# index return the index of substring
# but if it doesn't exist, error!
# find: returns the index of first occurrence of substring
# no match will return -1
print(city.index("v"))
print(city.index("ver"))
print(city.find("v"))
print(city.find("ver"))
print(city.find("x"))
print("*" * 40)

# count: return the occurrences of substring in string
# case-sensitive (0) vs case-insensitive (X)
greetings = "hello hello hello"
print(greetings.count("hello"))
print("*" * 40)

# Cheking characters in string
# isalnum() checks alphanumeric characters (alphabets + numbers)
# isalpha() checks if all characters are alphabets
# isdigit() checks digit characters
# isupper() checks if characters are uppercase
# islower() checks if characters are lowercase
# isspace() (space , tab \t, newine \n)

str = "hello "
number = "24"
print(number.isdigit())
print(str.isalnum())
print(str.isalpha())
print(str.isupper())
print(str.islower())
print(str.isspace())
