#!/usr/bin/env python3

import sys


def is_valid_1(num: int) -> bool:
    """Given an int, determine if it is an invalid num based on Part One"""
    num_str = str(num)
    num_len = len(num_str)
    num_mid = num_len // 2
    if num_len % 2 != 0:
        return False
    a, b = num_str[:num_mid], num_str[num_mid:]

    return a == b


def get_divisors(num: int) -> list[int]:
    divisors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def is_valid(num: int) -> bool:
    """Given an int, determine if it is an invalid num"""
    num_str = str(num)
    num_len = len(num_str)
    divisors = get_divisors(num_len)

    for d in divisors:
        pattern = num_str[:d]
        if pattern * (num_len // d) == num_str:
            return True
    return False


def main():
    inp = [line.strip() for line in sys.stdin.readlines()]
    id_ranges = inp[0].split(',')

    invalid_sum = 0

    for id_range in id_ranges:
        start, end = [int(x) for x in id_range.split('-')]

        for num in range(start, end + 1):
            if is_valid(num):
                invalid_sum += num

    print(invalid_sum)


if __name__ == '__main__':
    main()
