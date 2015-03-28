#!/usr/bin/env python

# 1/x + 1/y = 1/n
# n*x + n*y = x*y
# (x - n)*(y - n) = n**2

# For each factor f <= n dividing
# n**2 we'll get a unique solution.
# Since n**2 is a square, there will
# be an odd number of factors, hence
# if there are F(n) factors we will
# have (F(n) - 1)/2 pairs where f1 != f2,
# f1*f2 = n**2 and then f1 = f2 = n
# So we have (F(n) + 1)/2 solutions

import operator

from itertools import product as i_product

from python.decorators import euler_timer
from python.functions import power_up_to_digits
from python.functions import prime_factors
from python.functions import sieve


def main(verbose=False):
    prime_factors_hash = {}

    MINIMUM_SOLUTIONS = 4 * (10 ** 6)
    # P^k < 10**7 (10 mil)
    powers = [power_up_to_digits(prime, 7)
              for prime in [3, 5, 7]]
    products = [reduce(operator.mul, triple) for
                triple in list(i_product(*powers))]
    products = [product for product in sorted(products)
                if product > 2 * MINIMUM_SOLUTIONS][:20]

    PRIMES = sieve(100)

    max_prod = 10 ** 21
    res = []
    for product in products:
        factors = prime_factors(product, unique=False,
                                hash_=prime_factors_hash)
        factors = [(factor - 1) / 2 for factor in factors][::-1]
        curr_prod = 1
        for i, exp in enumerate(factors):
            curr_prod = curr_prod * (PRIMES[i] ** exp)

        if curr_prod < max_prod:
            max_prod = curr_prod

    return max_prod

if __name__ == '__main__':
    print euler_timer(110)(main)(verbose=True)
