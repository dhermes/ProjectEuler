#!/usr/bin/env python

# p_1^2 + p_2^3 + p_3^4 = n

from python.decorators import euler_timer
from python.functions import sieve


def max_p(k, n):
    return int(n ** (1.0 / k))


def relevant_triples(n):
    result = []
    top_sieve = sieve(max_p(2, n))
    next3 = [prime for prime in top_sieve
             if prime <= max_p(4, n)]
    for p3 in next3:
        next2 = [prime for prime in top_sieve
                  if prime <= max_p(3, n - p3 ** 4)]
        for p2 in next2:
            next1 = [prime for prime in top_sieve
                     if prime <= max_p(2, n - p3 ** 4 - p2 ** 3)]
            for p1 in next1:
                if p1 ** 2 + p2 ** 3 + p3 ** 4 < n:
                    result.append(p1 ** 2 + p2 ** 3 + p3 ** 4)
    return set(result)


def main(verbose=False):
    return len(relevant_triples(5 * 10 ** 7))

if __name__ == '__main__':
    print euler_timer(87)(main)(verbose=True)
