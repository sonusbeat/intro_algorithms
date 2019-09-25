""" Primes, GCD, LCM """
import math


def is_prime(n):
    """ Check if n is prime """
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """ GCD of a and b """
    smaller = b if a > b else a

    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd


def lcm(a, b):
    """ LCM of a and b """
    bigger = a if a > b else b

    while(True):
        if bigger % a == 0 and bigger % b == 0:
            lcm = bigger
            break
        bigger += 1
    return lcm


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    primes_numbers = []

    for number in range(2, n):
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False

        if is_prime:
            primes_numbers.append(number)

    return primes_numbers