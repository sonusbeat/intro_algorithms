age = int(input("Enter your age: "))

if age > 50:
    print("age > 50")
# 55

# This one value every single time
# if age > 40:
#     print("age > 50")
# if age > 40:
#     print("age > 40")
# if age > 30:
#     print("age > 30")
# if age > 20:
#     print("age > 20")
# if age > 10:
#     print("age > 10")

# This one value only once
if age < 50:
    if age == 45:
        print("age == 50")
    else:
        print("age > 40")
elif age > 40:
    print("age > 30")
elif age > 30:
    print("age > 20")
elif age > 20:
    print("age > 10")
elif age > 10:
    print("age > 0")
