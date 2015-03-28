#!/usr/bin/env python

# Find the sum of all numbers, less than one million, which
# are palindromic in base 10 and base 2.

from python.decorators import euler_timer
from python.functions import is_palindrome


def binary_incrementer(str_):
    digs = [int(dig) for dig in str_]
    digs[-1] += 1
    for i in range(len(digs) - 1, -1, -1):
        if digs[i] > 1:
            temp = digs[i]
            digs[i] = temp % 2
            if i == 0:
                digs = [temp / 2] + digs
            else:
                digs[i - 1] += temp / 2  # int division intended
        else:
            break
    return ''.join(str(dig) for dig in digs)


def all_base10_base2_palindromes(n):
    result = []
    base_10 = 1
    base_2 = '1'

    while base_10 < n:
        if is_palindrome(base_10) and is_palindrome(base_2):
            result.append(base_10)
        base_10 += 1
        base_2 = binary_incrementer(base_2)
    return result


def main(verbose=False):
    ans = all_base10_base2_palindromes(10 ** 6)
    if verbose:
        return '%s.\nThe full list of palindromes is: %s' % (
            sum(ans), ', '.join(str(number) for number in ans))
    else:
        return sum(ans)

if __name__ == '__main__':
    print euler_timer(36)(main)(verbose=True)
