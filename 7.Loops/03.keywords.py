# break: stop!
# break out the loop if there's number 4
# print numbers before 4
items = [12, 1, 5, 4, 16, 21, 6, 3, 8, 7]
print("BREAK")
for item in items:
    if item == 21:
        break
    print(item)

print('CONTINUE')
# continue: skip!
for item in items:
    if item == 21:
        continue
    print(item)
