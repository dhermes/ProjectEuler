#!/usr/bin/env python

# Since M(2**n + 1) = 4**n + 3**n - 2**(n + 1) (empirically),
# we find sum_{n=0}^{P} M(2**n + 1) is equal to
# (4**(P + 1) - 1)/3 + (3**(P + 1) - 1)/2 + 2*(2**(P + 1) - 1)
# = (4*(4**P) - 1)*(3**(-1)) + (3*(3**P) - 1)*(2**(-1)) + 4*(2**P) - 2
# (This is because (r - 1)*(r**P + ... + r + 1) = r**(P + 1) - 1

from python.decorators import euler_timer
from python.functions import inverse_mod_n


def moves(n):
    if n < 3:
        return n
    goal_state = [1] * n
    state = [0, 2] + [1] * (n - 2)
    num_moves = 1
    last_placed = 1

    while state != goal_state:
        beans = state[last_placed]
        state[last_placed] = 0
        for bean in range(1, beans + 1):
            next_index = (last_placed + bean) % n
            state[next_index] += 1
        last_placed = (last_placed + beans) % n
        num_moves += 1

    return num_moves


def check_formula(n):
    return (moves(2 ** n + 1) == 4 ** n - 3 ** n + 2 ** (n + 1))


# Since (a**(n**k))**n = a**(n*(n**k)) = a**(n**(k + 1)),
# We can easily compute X**(P + 1) = X*(X**P) for P = 10**18
def modular_exponentiate(val, exp_base, exp_power, modulus):
    result = val
    for i in xrange(exp_power):
        result = (result ** exp_base) % modulus
    return result


def main(verbose=False):
    for n in range(10):
        if not check_formula(n):
            raise Exception("Proposed formula for M(2**k + 1) incorrect.")

    modulus = 7 ** 9
    p_2 = 4 * modular_exponentiate(2, 10, 18, modulus) - 2
    p_3 = 3 * modular_exponentiate(3, 10, 18, modulus) - 1
    p_4 = 4 * modular_exponentiate(4, 10, 18, modulus) - 1

    return (p_4 * inverse_mod_n(3, modulus) -
            p_3 * inverse_mod_n(2, modulus) + p_2) % (modulus)

if __name__ == '__main__':
    print euler_timer(335)(main)(verbose=True)
