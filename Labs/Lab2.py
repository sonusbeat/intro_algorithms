"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """

    if nums[0] == 6:
        return True
    elif nums[-1] == 6:
        return True
    else:
        return False

def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    if len(nums) > 0 and nums[0] == nums[-1]:
        return True
    else:
        return False


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    result = 0

    for number in nums:
        result += number

    return result

def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    first = nums.pop(0)
    nums += [first]

    return nums


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    nums.reverse()

    return nums


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    result = []
    for _ in range(3):
        if nums[0] > nums[-1]:
            result += [nums[0]]
        elif nums[-1] > nums[0]:
            result += [nums[-1]]
        elif nums[0] == nums[-1]:
            result += [nums[0]]
    return result


def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    return [nums[0], nums[-1]]


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    i = 0
    result = False

    while i < len(nums):
        if nums[i] == 2 or nums[i] == 3:
            result = True
        i += 1

    return result
