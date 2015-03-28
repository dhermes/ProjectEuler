#!/usr/bin/env python

# Algorithm:
# Each pair of points defines a line
# Of these three lines, exactly two will cross the origin at an
# x value between the points defining the line
# The two lines that cross the origin define the range at y = 0

from python.decorators import euler_timer
from python.functions import get_data


def get_points(line):
    result = [int(val) for val in line.split(",")]
    return [(result[2 * i], result[2 * i + 1]) for i in range(3)]


def cross_zero(p, q):
    if p[0] == q[0]:
        if 0 <= max(p[1], q[1]) and 0 >= min(p[1], q[1]):
            return (p[0], True)
        else:
            return (-10 ** 10, False)
    m = ((p[1] - q[1]) * 1.0) / (p[0] - q[0])
    b = p[1] - m * p[0]
    if m == 0:
        if p[1] != 0:
            return (-10 ** 10, False)
        else:
            return ((p[0], q[0]), True)
    zero_val = (-b * 1.0) / m
    if zero_val <= max(p[0], q[0]) and zero_val >= min(p[0], q[0]):
        return (zero_val, True)
    else:
        return (-10 ** 10, False)


def zero_in(points):
    a, b, c = points
    crosses = [cross_zero(a, b), cross_zero(b, c), cross_zero(c, a)]
    crosses = [cross[0] for cross in crosses if cross[1]]
    if len(crosses) == 0:
        return False
    elif len(crosses) == 1:
        M = max(crosses[0])
        m = min(crosses[0])
        return (0 >= m and 0 <= M)
    return (0 >= min(crosses) and 0 <= max(crosses))


def main(verbose=False):
    data = [get_points(line) for line in get_data(102).split("\n") if line]
    count = 0
    for points in data:
        if zero_in(points):
            count += 1
    return count

if __name__ == '__main__':
    print euler_timer(102)(main)(verbose=True)
