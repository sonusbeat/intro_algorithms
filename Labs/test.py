def sort_half(alist):
    list_count = len(alist)
    middle_index = ((list_count // 2) + 1)
    for scan in range(list_count):
        swapped = False
        for j in range((list_count - 1) - scan):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True

        for scan in range(list_count):
            swapped = False
            for j in range((list_count - 1) - scan):
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
                    swapped = True

    return alist

    return middle_index

print(sort_half([5, 4, 6, 2, 1, 3, 8, -1]))