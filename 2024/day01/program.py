#!/usr/bin/env python3

import sys
from collections import Counter


def parse_input(inp):
    pairs = [(int(x), int(y)) for x, y in (line.strip().split('   ') for line in inp)]
    return list(zip(*pairs))


def part1(nums1, nums2):
    return sum(abs(x - y) for x, y in zip(sorted(nums1), sorted(nums2)))


def part2(nums1, nums2):
    counter = Counter(nums2)
    return sum(num * counter[num] for num in nums1)


def main():
    inp = [line.strip() for line in sys.stdin.readlines()]

    nums1, nums2 = parse_input(inp)

    print(part1(nums1, nums2))

    print(part2(nums1, nums2))

    print('hello')
    print('hi')


if __name__ == '__main__':
    main()
