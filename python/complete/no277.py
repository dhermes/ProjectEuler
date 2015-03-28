#!/usr/bin/env python

# D: x --> x/3 ==> D**(-1): y --> 3*y
# U: x --> (4*x + 2)/3 ==> U**(-1): y --> (3*y - 2)/4
# d: x --> (2*x - 1)/3 ==> d**(-1): y --> (3*y + 1)/2

# Starting with a_1, if we have any sequence (x_1,x_2,...,x_n)=s
# then a_{n + 1} = s(a_1) = x_n(...(x_2(x_1(a_1)))),
# forcing a_1 = x_1**(-1)(x_2**(-1)(...(x_n**(-1)(a_{n + 1}))))
# Clearly from composing D**(-1), U**(-1), and d**(-1), we'll get
# a function which f:y --> ((3**A)*y + B)/C for some values
# A, B, C. Initially with y, A = 0, B = 0 and C = 1
# NOTE: C will always be a power of 2

# Hence given s = (x_1,...) we can construct x**(-1) and easily
# update A, B and C based on the choice of each x_1

from python.decorators import euler_timer
from python.functions import inverse_mod_n


def sequence(letters, p_3, c, P_2):
    if letters == '':
        return p_3, c, P_2

    to_apply = letters[-1]
    if to_apply == 'D':
        return sequence(letters[:-1], p_3 + 1, 3 * c, P_2)
    elif to_apply == 'U':
        return sequence(letters[:-1], p_3 + 1, 3 * c - 2 * P_2, 4 * P_2)
    elif to_apply == 'd':
        return sequence(letters[:-1], p_3 + 1, 3 * c + P_2, 2 * P_2)


def main(verbose=False):
    p_3, c, P_2 = sequence('UDDDUdddDDUDDddDdDddDDUDDdUUDd', 0, 0, 1)
    # Here a_1 = s**(-1)(y) = ((3**(p_3))*y + c)/P_2
    # Since we need a_1 > 10**15, (3**(p_3))*y > (10**15)*P_2 - c
    min_y = ((10 ** 15) * P_2 - c) / (3 ** p_3)

    # We also need (3**(p_3))*y == -c mod P_2
    y_residue = inverse_mod_n(3 ** (p_3), P_2) * (-c) % P_2

    # integer division intended to find nearest multiple of P_2
    y = P_2 * (min_y / P_2) + y_residue
    if y < min_y:
        y += P_2

    return ((3 ** p_3) * y + c) / P_2

if __name__ == '__main__':
    print euler_timer(277)(main)(verbose=True)
