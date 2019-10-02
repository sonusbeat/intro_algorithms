""" Group Exercise Triple steps """


def triple_steps(n):
    """
    A child is running up a staircase with n steps and can hop
    either 1 step, 2 steps, or 3 steps at a time.
    Count how many possible ways the child can run up the stairs.
    :param n: the number of stairs
    :return: The number of possible ways the child can run up the stairs.
    """
    if n <= 2:
        return n

    return triple_steps(n-1) + triple_steps(n-2) + triple_steps(n-3)


print(triple_steps(3))