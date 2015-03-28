#!/usr/bin/env python

from math import sqrt

from python.decorators import euler_timer
from python.conway_topograph import next_juncture_on_river
from python.conway_topograph import juncture_isom


def minimal_solution(D):
    B = ((1, -1), 1 - D)
    P = ((1, 0), 1)
    N = ((0, 1), -D)
    F = ((1, 1), 1 - D)
    J_init = (B, P, N, F)
    J_curr = next_juncture_on_river(J_init)
    while not juncture_isom(J_init, J_curr):
        J_curr = next_juncture_on_river(J_curr)
    # since J = (B, P, N, F) the positive will
    # be at J[1]. Since P = ((x, y), val) and
    # We seek only (x,y), we want J[1][0]
    return J_curr[1][0]


def main(verbose=False):
    max_n = 1000
    non_squares = [n for n in range(1, max_n + 1) if n != int(sqrt(n)) ** 2]
    D_x_pair_min_solns = [(D, ) + minimal_solution(D) for D in non_squares]
    D_x_pair_min_solns.sort(key=lambda pair: pair[1])
    D, x, y = D_x_pair_min_solns[-1]
    if verbose:
        return "%s.\n%s^2 - %s*%s^2 = 1" % (D, x, D, y)
    else:
        return D

if __name__ == '__main__':
    print euler_timer(66)(main)(verbose=True)
