#!/usr/bin/env python

# The "Pentagonal Number Theorem" (a recurrence for the
# partition function) states:

#  p(k) = p(k - 1) + p(k - 2) - p(k - 5) - p(k - 7) + p(k - 12) + p(k - 15)

# where p(0) is taken to equal 1, p(k) is zero for negative k, and the sum is
# taken over all generalized pentagonal numbers of the form (n*(3*n-1))/2
# for n running over positive and negative integers (successively taking
# n = 1, -1, 2, -2, 3, -3, ...) generates the values 1, 2, 5, 7, 12, 15, ...
# The signs in the summation continue to alternate +, +, -, -, +, +

# for 1 <= k < 2, p(k) = p(k - 1)
# for 2 <= k < 5, p(k) = p(k - 1) + p(k - 2)
# for 5 <= k < 7, p(k) = p(k - 1) + p(k - 2) - p(k - 5)
# etc.
# With this in mind, we calculate the partition values for each
# segment until we find one congruent to 0 mod 10**6

from python.decorators import euler_timer
from python.functions import polygonal_number


def find_residue(residue):
    p = {0: 1}

    pentagonal = []
    pent_index = 1
    found_match = False
    while not found_match:
        if pent_index > 0:
            next_index = -pent_index
        else:
            next_index = abs(pent_index) + 1

        begin_val = polygonal_number(5, pent_index)
        end_val = polygonal_number(5, next_index)
        pentagonal.append(begin_val)
        for n in range(begin_val, end_val):
            # doesn't include end_val
            p[n] = 0
            for index, val in enumerate(pentagonal):
                if (index / 2) % 2 == 0:
                    p[n] = (p[n] + p[n - val]) % residue
                else:
                    p[n] = (p[n] - p[n - val]) % residue

            if p[n] == 0:
                found_match = True
                return n
        pent_index = next_index

    raise Exception("Should not reach this line")


def main(verbose=False):
    return find_residue(10 ** 6)

if __name__ == '__main__':
    print euler_timer(78)(main)(verbose=True)
