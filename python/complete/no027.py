#!/usr/bin/env python

# Using computers, the incredible formula  n^2 + 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values n = 0 to 79. The
# product of the coefficients, 79 and 1601, is 126479.

# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| < 1000

# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

# f(n + k) = (n + k)^2 + a(n + k) + b = f(n) + k^2 + ak + 2kn

# Need b prime since f(0) = b, largest value is 997
# We cheat and know n <= 79 since |b| < 1000
# Hence |f(n)| <= |n|^2 + |a||n| + |b| <= 6241 + 79(1000) + 997 = 86238

# Therefore, the biggest we ever have to worry about is 86238

from python.decorators import euler_timer
from python.functions import sieve


def polynomial_consecutive_primes(a, b, primes):
    # f(n + 1) = f(n) + 1 + a + 2n
    current = b
    index = 0
    while current in primes:
        current += 1 + a + 2 * index
        index += 1
    return index


def main(verbose=False):
    PRIMES = sieve(86238)
    b_choices = [prime for prime in PRIMES if prime < 1000]

    candidates = [(a, b, polynomial_consecutive_primes(a, b, PRIMES))
                  for a in range(-999, 999 + 1)
                  for b in b_choices]
    quantities = [entry[2] for entry in candidates]
    winner = candidates[quantities.index(max(quantities))]
    prod = winner[0] * winner[1]
    a = winner[0]
    b = winner[1]
    max_vals = winner[2]

    if verbose:
        return ('%s.\nSetting a = %s and b = %s produces '
                '%s consecutive primes.' % (prod, a, b, max_vals))
    else:
        return prod

if __name__ == '__main__':
    print euler_timer(27)(main)(verbose=True)
