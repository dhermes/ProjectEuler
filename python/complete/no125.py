#!/usr/bin/env python

# The palindromic number 595 is interesting because it can be written
# as the sum of consecutive squares:
# 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2

# There are exactly eleven palindromes below one-thousand that can
# be written as consecutive square sums, and the sum of these palindromes
# is 4164. Note that 1 = 0**2 + 1**2 has been excluded.

# Find the sum of all the numbers less than 10**8 that are both palindromic
# and can be written as the sum of consecutive squares.

# NOTE: I am assuming we need at least 2 squares, i.e. 121 = 11**2 doesn't
# count this assumption is because the use of plural in the question

from math import sqrt

from python.decorators import euler_timer
from python.functions import is_palindrome


def palindromic_square_sums(n):
    # first populate all pairs that add to less than n
    # 2k**2 < k**2 + (k + 1)**2 < n
    MAX_k = int(round(sqrt(n / 2.0)))
    curr = [index ** 2 + (index + 1) ** 2 for index in range(1, MAX_k)]
    curr = [num for num in curr if num < n]

    result = [num for num in curr if is_palindrome(num)]
    num_squares = 2
    while curr:
        num_squares += 1
        curr = [curr[i] + (i + num_squares) ** 2 for i in range(len(curr))]
        curr = [num for num in curr if num < n]
        result.extend([num for num in curr if is_palindrome(num)])

    return set(result)


def main(verbose=False):
    PROBLEM_MAX = 10 ** 8
    return sum(palindromic_square_sums(PROBLEM_MAX))

if __name__ == '__main__':
    print euler_timer(125)(main)(verbose=True)
