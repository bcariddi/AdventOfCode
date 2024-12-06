#!/usr/bin/env python3

import sys
import numpy as np
from copy import deepcopy


"""
Turn right 90 degrees:
    - up    -> right
    - right -> down
    - down  -> left
    - left  -> up
"""

DIRECTIONS = {
    'N': np.array([-1, 0]),
    'E': np.array([0, 1]),
    'S': np.array([1, 0]),
    'W': np.array([0, -1]),
}

ROT_DIRECTIONS = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}


def is_valid_position(grid, pos):
    rows, cols = grid.shape
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


def find_starting_position(grid):
    return np.argwhere(grid == '^')[0]


def get_next_position(pos, direction):
    return pos + DIRECTIONS[direction]


def move(grid, pos, direction):
    original_direction = direction

    while True:
        next_pos = get_next_position(pos, direction)

        if not is_valid_position(grid, next_pos):
            return pos, direction

        next_value = grid[tuple(next_pos)]

        if next_value != '#':
            return next_pos, direction

        direction = ROT_DIRECTIONS[direction]

        # If we're back to our original direction, we're stuck
        if direction == original_direction:
            return pos, direction


def route(grid, starting_position):
    pos = starting_position
    direction = 'N'

    visited = {tuple(pos)}

    while True:
        new_pos, new_direction = move(grid, pos, direction)

        # If we didn't move, which means we reached a boundary
        if np.array_equal(new_pos, pos):
            break

        visited.add(tuple(new_pos))

        pos, direction = new_pos, new_direction

    return visited


def detect_loop(grid, start_pos):
    pos = start_pos
    direction = 'N'

    visited_states = set()

    while True:
        state = (pos[0], pos[1], direction)

        if state in visited_states:
            return True

        visited_states.add(state)

        new_pos, new_direction = move(grid, pos, direction)

        # If we didn't move, which means we reached a boundary
        if np.array_equal(new_pos, pos):
            return False

        pos, direction = new_pos, new_direction


def find_loop_obstructions(grid, start_pos, visited_positions):
    loop_obstructions = []
    rows, cols = grid.shape

    # Only check positions that were visited in the original path
    for pos in visited_positions:
        row, col = pos
        if grid[row, col] == '#' or (row, col) == tuple(start_pos):
            continue

        test_grid = deepcopy(grid)
        test_grid[row, col] = '#'

        if detect_loop(test_grid, start_pos):
            loop_obstructions.append((row, col))

    return loop_obstructions


def main():
    grid = np.array([list(l.strip()) for l in sys.stdin])

    starting_position = find_starting_position(grid)

    visited_positions = route(grid, starting_position)

    print(len(visited_positions))

    loop_obstructions = find_loop_obstructions(
        grid, starting_position, visited_positions
    )

    print(len(loop_obstructions))


if __name__ == '__main__':
    main()
