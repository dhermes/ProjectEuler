#!/usr/bin/env python

# Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the
# remainder when (p_n - 1)**n + (p_n + 1)**n is divided by p_n**2.

# For example, when n = 3, p_3 = 5, and 4**3 + 6**3 = 280 == 5 mod 25.

# The least value of n for which the remainder first exceeds 10**9 is 7037.

# Find the least value of n for which the remainder first exceeds 10**10.

# ALGORITHM
# As in 120,
# (a+1)**n + (a-1)**n == na + 1 + (-1)**n(1 - na) mod a**2
# If n even, (a+1)**n + (a-1)**n == 2 mod a**2
# If n odd, (a+1)**n + (a-1)**n == 2an mod a**2

# Clearly n even won't contribute to a positive result
# 2*p_n*n < (p_n)**2 <==> 2*n < p_n which occurs for all n > 4
# since p_5 = 11 > 2*5 and p must increase by at least 2
# while n only increases by 1

# In these cases, the remainder is simply 2*p_n*n
# To get 2*n*p_n > 10**10, we need p_n**2 > n*p_n > 5*(10**9)
# or p_n > 70710

from python.decorators import euler_timer
from python.functions import sieve


def main(verbose=False):
    # Since p_n > 70710, to be safe let's multiply by 10
    PRIMES = sieve(707100)
    # The odd primes are the even indices here
    prime_index = 1
    product = 2 * (1 * 2)  # p_1 = 2
    while product < 10 ** 10:
        prime_index += 2
        prime = PRIMES[prime_index - 1]
        product = 2 * (prime_index * prime)
    return prime_index

if __name__ == '__main__':
    print euler_timer(123)(main)(verbose=True)
