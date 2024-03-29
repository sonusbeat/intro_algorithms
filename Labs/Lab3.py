"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    return string.count("hi")

def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    return string.count("cat") == string.count("dog")

def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    total = 0

    for i in range(len(string) - 3):
        if string[i:i+2] == "co" and string[i+3] == "e":
            total += 1
    return total


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    # 1. make both string lowercase or uppercase
    # 2. get the length of two string and compare
    # 3. check if the shorter string appears at the end of longer string

    lowered_a = a.lower()
    lowered_b = b.lower()

    if len(lowered_a) > len(lowered_b):
        # last len(lowered) chars of lowered_a
        return lowered_a[-len(lowered_b):] == lowered_b
    elif len(lowered_a) == len(lowered_b):
        return lowered_a == lowered_b
    else:
        return lowered_b[-len(lowered_a):] == lowered_a


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1

    return count

def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    i = 0
    total = 0

    while i < len(nums):
        if nums[i] != 13:
            total += nums[i]
            i += 1
        else:
            i += 2
    return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    switch = True
    total = 0
    for num in nums:
        if num == 6 and switch == True:
            switch = False
            continue
        if num == 7 and switch == False:
            switch = True
            continue
        if switch == True:
            total += num

    return total

def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False


