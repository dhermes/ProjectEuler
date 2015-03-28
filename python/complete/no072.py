#!/usr/bin/env python

# neighbors
# a/b < c/d
# need bc - ad = 1

# The converse is also true. If
# bc - ad =  1
# for positive integers a,b,c and d with a < b and c < d then a/b and c/d
# will be neighbours in the Farey sequence of order max(b,d).

# How many elements would be contained in the set of reduced proper
# fractions for D <= 1,000,000?

#########################################################
# |F_n| = |F_(n-1)| + PHI(n)
# |F_0| = 1
# |F_n| = 1 + sum_{i in  1 to n} PHI(i)
# sum_{i in  1 to n} PHI(i)
# sum_{d|n} PHI(d) = n

# Algorithm 1:
# Kill off all factors of n
# Find max, kill off all factors
# Repeat

# MU(n) = 0 if n not square-free
#       else 1 if n is has an even number of prime factors
#       else -1 if n is has an odd number of prime factors
# 2*sum_{i in  1 to n} PHI(i) = 1 + sum_{i in  1 to n} MU(i) floor(n/i)**2

# Algorithm 2:
# 1. Generate all n <= 10**6 with 1 factors by listing possible subsets of
#         primes
# 2. Use formula

from math import floor
from math import sqrt

from python.decorators import euler_timer
from python.functions import mu
from python.functions import sieve


def main(verbose=False):
    D = 10 ** 6
    PRIMES = sieve(int(sqrt(D)) + 1)
    # We seek |F_D| = 1 + sum_{i in  1 to D} PHI(i)
    # 2*sum_{i in  1 to D} PHI(i) = 1 + sum_{i in  1 to D} MU(i) floor(D/i)**2
    # 2*|F_D| = 3 + sum_{i in  1 to D} MU(i) floor(D/i)**2
    mu_hash = {1: 1}
    running_sum = D ** 2  # i = 1
    for i in range(2, D + 1):
        running_sum += mu(i, mu_hash, PRIMES) * (int(floor(D * 1.0 / i)) ** 2)

    # They don't include 0/1 or 1/1 so we subtract 2
    return ((3 + running_sum) / 2 - 2)

if __name__ == '__main__':
    print euler_timer(72)(main)(verbose=True)
