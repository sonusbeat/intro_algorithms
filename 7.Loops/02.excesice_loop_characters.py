# Exercise

# Print the names that have less than 5 characters from the given list.

names = [
    "Derrick", "Diego", "Rick",
    "Richard", "Anzu", "Wenda",
    "Yusuke", "Ryo", "Bianca",
    "Tae", "Kam", "Elen",
    "Naoki", "Shohei", "Hotsuma",
    "Yuka", "Mika", "Douglas",
    "Gabriel"
]

# for name in (names):
#     if len(name) < 5:
#         print(name)

# 2^0 + 2^1 + ... + 2^30
answer = 0
for i in range(31):
    answer += (2 ** i)

print(answer)
print(2 ** 31 - 1)