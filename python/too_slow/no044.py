#!/usr/bin/env python

# Pentagonal is n(3n-1)/2
# Find (j,k) for which P_j + P_k and abs(P_j - P_k) = D is pentagonal and D is minimized. What is D?

# We will infinitely generate (k,j) = (1,2), (1,3), (2,3), (1,4), (2,4), ...
# We will infinitely generate (k,j) = (1,2), (2,3), (1,3), (3,4), (2,4), (1,4), (4,5), ...
# Will check if P_j - P_k is pentagonal.
# If it is, will then check if P_k + P_j is

# NOTE: P_j - P_k is increasing in j and decreasing in k, so if we fix j, it is
# minimized when k is largest, i.e. P_j - P_(j - 1)
# = (3j**2 - j)/2 - (3(j - 1)**2 - (j - 1))/2 = 3j - 2

# For k < j, P_j - P_k >= 3j - 2
# So if we have established a difference D, if 3j - 2 >= D, we need not consider it,
# hence we need k < j < (D + 2)/3

from python.decorators import euler_timer
from python.functions import polygonal_number
from python.functions import reverse_polygonal_number


def increment_pair(pair):
    """
    Increments pair by traversing through all
    k for a given j until 1 is reached, then starting
    back up with the next highest value for j

    E.G. [1,2]-->[2,3]-->[1,3]-->[3,4]-->[2,4]-->...
    """
    k, j = pair
    k -= 1
    if k > 0:
        return [k, j]
    else:
        return [j, j + 1]


def main(verbose=False):
    # Not only finds the minimum, but also checks to make sure
    # it is the smallest. Since P_j - P_k >= P_j - P_(j-1) = 3j - 2
    # If 3j - 2 > D, then P_j - P_k > D, and we not longer need to
    # check the minimum
    pair = [1, 2]
    D = -1
    while D == -1 or 3 * pair[1] - 2 <= D:
        vals = [polygonal_number(5, val) for val in pair]
        difference = abs(vals[0] - vals[1])
        if D != -1 and difference > D:
            # since increment decreases the first argument, if
            # we go past the difference, we can stop checking
            # [k, j] for a fixed j, and we just bypass
            # by incrementing j
            last = pair[1]
            pair = [last, last + 1]
        else:
            if reverse_polygonal_number(5, difference) != -1:
                if reverse_polygonal_number(5, sum(vals)) != -1:
                    if D == -1 or difference < D:
                        D = difference
            pair = increment_pair(pair)
    return D

if __name__ == '__main__':
    print euler_timer(44)(main)(verbose=True)
