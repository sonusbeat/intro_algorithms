""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.

def sort_half(alist):
    for scan in range(len(alist)):
        swapped = False
        for j in range((len(alist) - 1) - scan):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = True

    list_a = alist[0:len(alist) // 2]
    list_b = alist[len(alist) // 2:]

    for scan in range(len(list_b)):
        swapped = False
        for j in range((len(list_b) - 1) - scan):
            if list_b[j] < list_b[j + 1]:
                list_b[j], list_b[j + 1] = list_b[j + 1], list_b[j]
                swapped = True

    return list_a + list_b


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    i = 0
    j = 0
    merged = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    return merged + A[i:] + B[j:]


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.

def replace_negative(mylist):
    i = 0
    while i < len(mylist):
        if mylist[i] < 0:
            mylist[i] = 0
        i += 1

    return mylist