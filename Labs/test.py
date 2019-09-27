def sum67(nums):
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