#!/usr/bin/env python3

import sys


def count_zero_hits(start, distance, direction):
    if distance == 0:
        return 0

    if direction == 'R':
        if start == 0:
            return distance // 100
        else:
            return (distance + start) // 100
    else:
        if start == 0:
            return distance // 100
        else:
            if distance >= start:
                return 1 + (distance - start) // 100
            else:
                return 0


def main():
    current = 50
    total_count = 0

    inp = [line.strip() for line in sys.stdin.readlines()]

    for rotation in inp:
        start = current
        direction, distance = rotation[0], int(rotation[1:])

        if direction == 'L':
            current = (current - distance) % 100
        else:
            current = (current + distance) % 100

        hits = count_zero_hits(start, distance, direction)
        total_count += hits

        # if hits > 0:
        #    print(
        #        f'HIT - Points at 0 {hits} time(s). Moved {distance} {direction} from {start} to {current}'
        #    )
        # else:
        #    print(f'Moved {distance} {direction} from {start} to {current}')

    print(total_count)


if __name__ == '__main__':
    main()
