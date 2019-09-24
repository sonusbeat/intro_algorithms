# Selection sort
# pseudo-code
# for each scan from 0 to len(collection)
#     find the min element (linear search)
#     swap the min element with collection[scan]

# Time complexity
# O(n^2)

def selection_sort(collection):
    steps = 0
    collection_count = len(collection)
    for scan in range(collection_count):
        min_index = scan
        for j in range(scan, collection_count):
            steps += 1
            if collection[min_index] > collection[j]:
                min_index = j

        # swap
        # collection[scan], collection[min_index] = collection[min_index], collection[scan]
        temp = collection[scan]
        collection[scan] = collection[min_index]
        collection[min_index] = temp
    print("steps:", steps)
    print("collection:", collection)


print("-" * 40)
print("Selection sort")
selection_sort([5, 1, 4, 2, 3])
print("-" * 40)
def selection_sort_improved(collection):
    steps = 0
    collection_count = len(collection)
    for scan in range(collection_count - 1):
        min_index = scan

        for j in range(scan + 1, collection_count):
            steps += 1
            if collection[min_index] > collection[j]:
                min_index = j

        # swap
        if min_index != scan:
            # collection[scan], collection[min_index] = collection[min_index], collection[scan]
            temp = collection[scan]
            collection[scan] = collection[min_index]
            collection[min_index] = temp

    print("steps:", steps)
    print("collection", collection)


print("Selection sort improved")
selection_sort_improved([5, 1, 4, 2, 3])
print("-" * 40)
