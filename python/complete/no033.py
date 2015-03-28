#!/usr/bin/env python

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator
# and denominator.

# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

import operator

from fractions import gcd

from python.decorators import euler_timer


def canceled_pair(numer, denom):
    shared = set(str(numer)).intersection(set(str(denom)))
    result_n = [dig for dig in str(numer)]
    result_d = [dig for dig in str(denom)]
    for dig in shared:
        result_n.remove(dig)  # Only removes first instance
        result_d.remove(dig)  # Only removes first instance
    result_n = int("".join(result_n)) if result_n else 0
    result_d = int("".join(result_d)) if result_d else 0
    return result_n, result_d


def equals_canceled_pair(numer, denom):
    c_num, c_denom = canceled_pair(numer, denom)
    if c_num == numer and c_denom == denom:
        return False
    elif 10 * c_num == numer:
        return False
    elif c_num == 0 and c_denom == 0:
        return False
    return (c_num * denom == c_denom * numer)


def main(verbose=False):
    pairs = [(numer, denom)
             for numer in range(10, 99)
             for denom in range(numer + 1, 100)
             if equals_canceled_pair(numer, denom)]
    num = reduce(operator.mul, [pair[0] for pair in pairs])
    denom = reduce(operator.mul, [pair[1] for pair in pairs])
    return denom / (gcd(num, denom))

if __name__ == '__main__':
    print euler_timer(33)(main)(verbose=True)
