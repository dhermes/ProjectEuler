#!/usr/bin/env python

# A_G(x) = xG_1 + x^2G_2 + ...
# (x + x^2)A_G(x) = x^2G_1 + x^3G_2 + ... + x^3G_1 + x^4G_2 + ...
# using G_k = G_{k-1} + G_{k-2}, G_1=1, G_2=4
# (x + x^2)A_G(x) = x^2G_1 + x^3G_3 + x^4G_4 + ..
# (x + x^2)A_G(x) = x^2G_1 - xG_1 - x^2G_2 + A_G(x)
# A_G(x) = (-x - 3x^2)/(x^2 + x - 1)

# A_G(x) = n ==> (n+3)x^2 + (n+1)x - n = 0
# For x to be rational, we need to discriminant sqrt(b^2 - 4ac)
# to be rational
# D = (n + 1)^2 - 4(n + 3)(-n) = 5n^2 + 14n + 1 = m^2
# 25n^2 + 70n + 49 = 5m^2 + 44
# (5n + 7)^2 - 5m^2 = 44

from python.conway_topograph import all_values_on_form
from python.conway_topograph import get_recurrence
from python.conway_topograph import start_to_series
from python.decorators import euler_timer
from python.functions import recurrence_next


def golden_nuggets(limit):
    # We seek x_k^2 - 5y_k^2 = 44
    # Where 5n + 7 = x_k
    x_mult, y_mult, relation = get_recurrence([1, -5])
    starting_points = all_values_on_form([1, -5], 44)
    series = [start_to_series(initial, x_mult, 'x')
              for initial in starting_points]
    nuggets = [pair[0] for pair in series
               if pair[0] % 5 == 2 and pair[0] > 7]
    while len(nuggets) < 2 * limit:
        next = [pair[1] for pair in series
                if pair[1] % 5 == 2 and pair[1] > 7]
        nuggets.extend(next)
        series = [recurrence_next(relation, values) for values in series]
    return sorted([(value - 7) / 5 for value in nuggets])[:limit]


def main(verbose=False):
    nuggets = golden_nuggets(30)
    if verbose:
        return '%s.\nAs a check, the 20th golden nugget is calculated ' \
               'to be %s, as stated.' % (sum(nuggets), nuggets[20 - 1])
    else:
        return sum(nuggets)

if __name__ == '__main__':
    print euler_timer(140)(main)(verbose=True)
