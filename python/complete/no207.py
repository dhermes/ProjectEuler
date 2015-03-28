#!/usr/bin/env python

# Let X = 2**t, then X**2 = 4**t = X + k
# 4X**2 - 4X + 1 = 4k + 1
# 4*k + 1 must be a perfect square
# k = n(n + 1) for some n > 0 (since k > 0)

# t is an integer if X is a power of 2
# but X = (1 + sqrt(4k + 1))/2
# but X = (1 + 2*n + 1)/2 = n + 1
# So we need n + 1 = 2**p for a power of p
# in order for the count to change

# When n = 2**L - 1, we have L total perfect
# <= n, hence P(n) = L/(2**L - 1)
# We seek the first such (n, L) with P(n) < 1/12345
# i.e. 12345*L + 1 < 2**L, so the ratio makes
# its first switch over between 2**(L - 1) - 1
# and 2**L - 1. So we set the initial value
# to L - 1 and loop from 2**(L - 1) to 2**L - 1
# to find where the threshold breaks

from python.decorators import euler_timer


def main(verbose=False):
    L = 1
    while 12345 * L + 1 >= 2 ** L:
        L += 1

    count = L - 1
    for n in range(2 ** (L - 1), 2 ** L):
        if 12345 * count < n:
            return n * (n + 1)
    raise Exception("Program failed to find solution")

if __name__ == '__main__':
    print euler_timer(207)(main)(verbose=True)
