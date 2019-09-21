# String (str) : A sequence of characters in "" or ''
# Concatenation: combining two string: "hello" + " world"
# * multiplication: repeat strings
print("hello\n" * 5)

# String indexing (position)
singer = "Justin Bieber"

print(singer[7])  # "B"
print(singer[-6])  # "B"
print(singer[-1])  # r last character
# print(singer[-14])  # error (out of index)

# String slicing
# index
# [start index : end index]
# end of index is not inclusive
actor = "Brad Pitt"
print(actor[0:3])  # Bra
print(actor[0:4])  # Brad

# shortcuts
# starting at 0 index
print(actor[:4])

# starting at 5 to the end.
print(actor[5:])

# from 0 to the end (copy)
print(actor[:])

# get ASCI number
print(ord("a"[0]))
print(ord("A"[0]))

# How to get the number of characters
# actor's last index: len -1
print(len(actor))

# Get the last character
print(actor[-1])
print(actor[len(actor)-1])
print(actor[8])
# https://www.youtube.com/watch?v=_uQrJ0TkZlc