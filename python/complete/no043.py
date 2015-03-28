#!/usr/bin/env python

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.

# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
# note the following:

# d_2 d_3 d_4 = 406 is divisible by 2
# d_3 d_4 d_5 = 063 is divisible by 3
# d_4 d_5 d_6 = 635 is divisible by 5
# d_5 d_6 d_7 = 357 is divisible by 7
# d_6 d_7 d_8 = 572 is divisible by 11
# d_7 d_8 d_9 = 728 is divisible by 13
# d_8 d_9 d_10 = 289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

# Since 5 | d_4 d_5 d_6, we know d_6 in [0,5]
# Since 11 | d_6 d_7 d_8 in [0 d_7 d_8, 5 d_7, d_8], we know d_6 = 5
# This is because the only multiples of 11 with d_6 = 0 are
# 11, 22, ..., 99, all of which have repeated digits
# 11*50 = 550 is also eliminated, leaving us with
# d_6 d_7 d_8 in [506, 517, 528, 539, 561, 572, 583, 594]

import operator

from python.decorators import euler_timer


def extend_matches(value, choices, direction):
    """
    Extends the value by anything in choices the
    1) ends in the same 2 digits that value begins with
    2) has remaining digit(s) unique from those in value
    """
    value_digits = set(value)
    if direction == 'right':
        first_two_match = [choice for choice in choices
                           if choice[:2] == value[-2:]]
        matches = [choice for choice in first_two_match
                   if value_digits.intersection(choice[2:]) == set()]
        return [value + choice[2:] for choice in matches]
    elif direction == 'left':
        last_two_match = [choice for choice in choices
                          if choice[-2:] == value[:2]]
        matches = [choice for choice in last_two_match
                   if value_digits.intersection(choice[:-2]) == set()]
        return [choice[:-2] + value for choice in matches]
    else:
        raise ValueError("%s not a valid direction." % direction)


def extend_to_remaining_digit(value):
    last_digit = set('0123456789').difference(value)
    if len(last_digit) != 1:
        raise ValueError("Algorithm for 43 failed.")
    last_digit = last_digit.pop()
    return int(last_digit + value)


def main(verbose=False):
    unique_digits = {}
    primes = [2, 3, 5, 7, 11, 13, 17]
    for prime in primes:
        mults = [str(number).zfill(3) for number in range(1, 1000)
                 if number % prime == 0]
        unique_digits[prime] = [number for number in mults
                                if len(set(number)) == 3]
    candidates = [number for number in unique_digits[11] if number[0] == '5']

    # We have only covered the 11 case, so we need to include those for the
    # 13 and 17 to the right and 7, 5, 3, 2 to the left (in order)
    for prime in [13, 17]:
        candidates = reduce(operator.add,
            [extend_matches(candidate, unique_digits[prime], 'right')
             for candidate in candidates])
    for prime in [7, 5, 3, 2]:
        candidates = reduce(operator.add,
            [extend_matches(candidate, unique_digits[prime], 'left')
             for candidate in candidates])
    # We now have all possibilities for d_2 ... d_10, from which we can
    # generate d_1
    candidates = [extend_to_remaining_digit(candidate)
                  for candidate in candidates]
    return sum(candidates)

if __name__ == '__main__':
    print euler_timer(43)(main)(verbose=True)
