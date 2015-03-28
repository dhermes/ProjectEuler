#!/usr/bin/env python

# By solving all fifty puzzles find the sum of the 3-digit numbers
# found in the top left corner of each solution grid; for example,
# 483 is the 3-digit number found in the top left corner of the
# solution grid above.

import operator

from python.decorators import euler_timer
from python.functions import get_data
from python.sudoku import make_generators
from python.sudoku import stack_assumptions
from python.sudoku import Sudoku


def corner_sum(board):
    sudoku = Sudoku(board)

    for _ in stack_assumptions(make_generators(sudoku)):
        first, second, third = sudoku.board[0][:3]
        return 100 * first + 10 * second + third


def main(verbose=False):
    puzzles = get_data(96).split("\n")
    puzzles = [reduce(operator.add, puzzles[10 * index + 1:10 * index + 10])
               for index in range(50)]
    return sum(corner_sum(puzzle) for puzzle in puzzles)

if __name__ == '__main__':
    print euler_timer(96)(main)(verbose=True)
