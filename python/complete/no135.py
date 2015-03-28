#!/usr/bin/env python

# Given the positive integers, x, y, and z, are consecutive terms of an
# arithmetic progression, the least value of the positive integer, n,
# for which the equation, x^2 - y^2 - z^2 = n, has exactly two solutions
# is n = 27:

# 34^2 - 27^2 - 20^2 = 12^2 - 9^2 - 6^2 = 27

# It turns out that n = 1155 is the least value which has exactly
# ten solutions.

# How many values of n less than one million have exactly
# ten distinct solutions?

###############################
# Positive integers, a > k > 0
# n = (a + k)^2 - a^2 - (a - k)^2
# n = a(4k - a)

# Pick a | n, then k = (n + a**2)/(4*a)
# We need k < a, so n = a(4k - a) < 3a**2
# We need k integral, so (n/a + a) % 4 == 0

from math import sqrt

from python.decorators import euler_timer
from python.functions import factors
from python.functions import sieve


def num_solutions(factor_list):
    n = max(factor_list)
    choices_a = [factor for factor in factor_list if n < 3 * (factor ** 2)]
    return [a for a in choices_a if (n / a + a) % 4 == 0]


def main(verbose=False):
    MAX_n = 10 ** 6 - 1
    distinct_solutions = 10
    PRIMES = sieve(int(sqrt(MAX_n)) + 1)
    factor_hash = {}

    count = 0
    for n in range(1, MAX_n + 1):
        factor_list = factors(n, factor_hash, PRIMES)
        if len(num_solutions(factor_list)) == distinct_solutions:
            count += 1
    return count

if __name__ == '__main__':
    print euler_timer(135)(main)(verbose=True)
