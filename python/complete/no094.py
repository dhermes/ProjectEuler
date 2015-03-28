#!/usr/bin/env python

# It is easily proved that no equilateral triangle exists with integral
# length sides and integral area. However, the almost equilateral
# triangle 5-5-6 has an area of 12 square units.

# We shall define an almost equilateral triangle to be a triangle for
# which two sides are equal and the third differs by no more than one unit.

# Find the sum of the perimeters of all almost equilateral triangles
# with integral side lengths and area and whose perimeters do not exceed
# one billion (1,000,000,000).

# We either have n-n-(n+1) or n-n-(n-1) as our triangle
# dropping a height h, we see n**2 = h**2 + ((n + sign)/2)**2
# ==> 3n**2 - 2*sign*n - 1= 4h**2
# ==> (3*n - sign)**2 - 4 = 9n**2 - 6*sign*n - 3 = 12h**2
# ==> (3*n - sign)**2 - 3(2h)**2 = 4

from python.conway_topograph import all_values_on_form
from python.conway_topograph import get_recurrence
from python.conway_topograph import start_to_series
from python.decorators import euler_timer
from python.functions import recurrence_next


def solutions(limit):
    # We seek x_k^2 - 3y_k^2 = 4
    # Where 3*n - sign = x_k
    x_mult, y_mult, relation = get_recurrence([1, -3])
    starting_points = all_values_on_form([1, -3], 4)
    series = [start_to_series(initial, x_mult, 'x')
              for initial in starting_points]
    result = [pair[0] for pair in series
              if pair[0] % 3 != 0 and pair[0] > 0]
    while max(result) < 2 * limit:
        next = [pair[1] for pair in series
                if pair[1] % 3 != 0 and pair[1] > 0]
        result.extend(next)
        series = [recurrence_next(relation, values) for values in series]
    # We seek perimeters n + n + (n + sign) = 3n + sign
    # We currently have 3n - sign, so if we can determine the sign
    # If value == 1 mod 3, then 3n - sign == 1, hence sign = -1
    # and 3n + sign = 3n - 1 = value - 2
    # If value == -1 mod 3, then 3n - sign == -1, hence sign = 1
    # and 3n + sign = 3n + 1 = value + 2
    result = sorted(((value + 2) if value % 3 == 2 else (value - 2))
                    for value in result)
    # The first two solutions are 1-1-0 and 1-1-2, which are both degenerate
    return [perimeter for perimeter in result
            if perimeter < limit and perimeter not in (2, 4)]


def main(verbose=False):
    # the first solutions up to a billion are returned in solutions(10**9)
    return sum(solutions(10 ** 9))

if __name__ == '__main__':
    print euler_timer(94)(main)(verbose=True)
