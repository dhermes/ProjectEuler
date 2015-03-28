#!/usr/bin/env python

# 2**N binary digits can be placed in a circle so that all the N-digit
# clockwise subsequences are distinct.

# For N=3, two such circular arrangements are possible, ignoring
# rotations:
# (0,0,0,1,0,1,1,1) and (0,0,0,1,1,1,0,1)

# For the first arrangement, the 3-digit subsequences, in clockwise
# order, are: 000, 001, 010, 101, 011, 111, 110 and 100.

# Each circular arrangement can be encoded as a number by concatenating
# the binary digits starting with the subsequence of all zeros as the
# most significant bits and proceeding clockwise. The two arrangements
# for N=3 are thus represented as 23 and 29:

# 00010111_2 = 23
# 00011101_2 = 29

# Calling S(N) the sum of the unique numeric representations, we can see
# that S(3) = 23 + 29 = 52.

# Find S(5).

###########################

# Since 2**N and it is a circular arrangement, all 2**N, N digit binaries
# must be present. Hence we start with [0]*N. Since it can only occur once
# we can actually pad it with ones on either side for [1] + [0]**N + [1]

from python.decorators import euler_timer


def binary_array_to_integer(array):
    result = 0
    for val in array:
        result = 2 * result + val
    return result


def has_unique_subsequences(array, length):
    values = []
    for i in range(len(array) - length + 1):
        to_add = binary_array_to_integer(array[i:i + length])
        if to_add in values:
            return False
        values.append(to_add)
    return True


def add_value(array, length):
    # may return []
    result = [array[:] + [new_val] for new_val in [0, 1]
              if has_unique_subsequences(array[:] + [new_val], length)]
    return result


def all_valid_sequences(length):
    sequences = [[1] + [0] * length + [1]]
    while len(sequences[0]) < 2 ** length:
        next_sequences = []
        for sequence in sequences:
            next_sequences.extend(add_value(sequence, length))
        sequences = next_sequences[:]
    # After this step, we want to make it cyclic, so we overload and check
    sequences = [sequence + sequence[:length - 1] for sequence in sequences]
    sequences = [sequence[:2 ** length] for sequence in sequences
                 if has_unique_subsequences(sequence, length)]
    # finally, we want to start at 0, but these all start at 1
    return [sequence[1:] + sequence[:1] for sequence in sequences]


def main(verbose=False):
    sequences = all_valid_sequences(5)
    return sum(binary_array_to_integer(sequence) for sequence in sequences)

if __name__ == '__main__':
    print euler_timer(265)(main)(verbose=True)
