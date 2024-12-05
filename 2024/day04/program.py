#!/usr/bin/env python3

import sys
import numpy as np


def is_valid_value(grid, row, col, letter):
    """
    Check if position is valid and contains expected letter value
    """
    rows, cols = grid.shape
    return 0 <= row < rows and 0 <= col < cols and grid[row, col] == letter


def check_sequence_after_m(grid, m_row, m_col, direction):
    """
    Check if A and S follow M in the same direction as X->M
    """
    a_row, a_col = m_row + direction[0], m_col + direction[1]
    if not is_valid_value(grid, a_row, a_col, 'A'):
        return False

    s_row, s_col = a_row + direction[0], a_col + direction[1]
    return is_valid_value(grid, s_row, s_col, 'S')


def count_from_x(grid, i, j):
    """
    Count XMASes starting from a given X position at i, j
    """
    count = 0
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            if is_valid_value(grid, x, y, 'M') and check_sequence_after_m(
                grid, x, y, (x - i, y - j)
            ):
                count += 1

    return count


def count_xmas(grid):
    """
    Count all XMASes in grid
    """
    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'X':
                total += count_from_x(grid, i, j)

    return total


def check_from_a(grid, i, j):
    """
    Check for an X shape from a given A position at i, j
    """
    is_x_top = (
        is_valid_value(grid, i - 1, j - 1, 'M')
        and is_valid_value(grid, i - 1, j + 1, 'M')
        and is_valid_value(grid, i + 1, j - 1, 'S')
        and is_valid_value(grid, i + 1, j + 1, 'S')
    )
    is_x_left = (
        is_valid_value(grid, i - 1, j - 1, 'M')
        and is_valid_value(grid, i - 1, j + 1, 'S')
        and is_valid_value(grid, i + 1, j - 1, 'M')
        and is_valid_value(grid, i + 1, j + 1, 'S')
    )
    is_x_bottom = (
        is_valid_value(grid, i - 1, j - 1, 'S')
        and is_valid_value(grid, i - 1, j + 1, 'S')
        and is_valid_value(grid, i + 1, j - 1, 'M')
        and is_valid_value(grid, i + 1, j + 1, 'M')
    )
    is_x_right = (
        is_valid_value(grid, i - 1, j - 1, 'S')
        and is_valid_value(grid, i - 1, j + 1, 'M')
        and is_valid_value(grid, i + 1, j - 1, 'S')
        and is_valid_value(grid, i + 1, j + 1, 'M')
    )
    return is_x_top or is_x_left or is_x_bottom or is_x_right


def count_x_mas(grid):
    """
    Count all X-MASes in grid
    """

    # NOTE: an X shape can be in any direction:
    #
    # M.M
    # .A.
    # S.S
    #

    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'A':
                # Each A can only have 0 or 1 X shapes
                total += check_from_a(grid, i, j)

    return total


def main():
    grid = np.array([list(l.strip()) for l in sys.stdin])

    print(count_xmas(grid))
    print(count_x_mas(grid))


if __name__ == '__main__':
    main()
