# Bubble Sort - "Bubbling" the largest element to the right
# (pseudo-code)
# list = [...]
# for each i from 1 to the len(list)
#     compare to adjacent elements
#     if the first element is greater than the second element
#         swap two elements

# Time Complexity
# O(n^2) algorithm

def bubble_sort(collection):
    steps = 0
    collection_count = len(collection)
    for scan in range(collection_count):
        for j in range(collection_count - 1):
            steps += 1
            if collection[j] > collection[j+1]:
                # swap
                collection[j], collection[j+1] = collection[j+1], collection[j]  # Only works on Python
                # temp = collection[j]
                # collection[j] = collection[j+1]
                # collection[j+1] = temp
    print("steps: ", steps)
    print("collection: ", collection)


print("-" * 40)
print("Bubble sort")
bubble_sort([5, 3, 2, 1, 4])
print("-" * 40)

def bubble_sort_improved(collection):
    steps = 0
    collection_count = len(collection)
    for scan in range(collection_count):
        swapped = False
        for j in range((collection_count - 1) - scan):
            steps += 1
            if collection[j] > collection[j + 1]:
                # swap
                collection[j], collection[j+1] = collection[j+1], collection[j]  # Only works on Python
                # temp = collection[j]
                # collection[j] = collection[j + 1]
                # collection[j + 1] = temp
                swapped = True
        if not swapped:
            break
    print("steps: ", steps)
    print("collection: ", collection)


print("Bubble sort improved")
bubble_sort_improved([5, 3, 2, 1, 4])
print("-" * 40)
