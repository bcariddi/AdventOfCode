#!/usr/bin/env python3

import sys


def get_joltage_v2(line: str) -> int:
    # the difference is that in part 1, we didn't have to worry too much
    # about the remaining length of the line

    joltage_string = ''

    max_val = max(line[:-11])
    i_max_val = line.index(max_val)

    remaining_line = line[i_max_val + 1 :]

    joltage_string += str(max_val)

    for i in range(10, -1, -1):
        if i == 0:
            max_val = max(remaining_line)
            i_max_val = remaining_line.index(max_val)
        else:
            remaining_line_cut_off = remaining_line[: -1 * i]
            max_val = max(remaining_line_cut_off)
            i_max_val = remaining_line_cut_off.index(max_val)

        remaining_line = remaining_line[i_max_val + 1 :]

        joltage_string += str(max_val)

    return int(joltage_string)


def get_joltage(line: str) -> int:
    # first, find the first occurence of the largest non-final digit
    # then, from [i_largest_non_final + 1 :], find the largest digit

    max_val = max(line[:-1])

    i_max_val = line.index(max_val)

    remaining_line = line[i_max_val + 1 :]
    remaining_max_val = max(remaining_line)

    return int(f'{max_val}{remaining_max_val}')


def main():
    inp = [line.strip() for line in sys.stdin.readlines()]

    joltage_sum = 0
    for line in inp:
        joltage = get_joltage_v2(line)
        joltage_sum += joltage

    print(joltage_sum)


if __name__ == '__main__':
    main()
