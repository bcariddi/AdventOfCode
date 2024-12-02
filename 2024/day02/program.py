#!/usr/bin/env python3

import sys


def find_unsafes(report, increasing=True):
    unsafe_indicies = set()

    for i, (a, b) in enumerate(zip(report, report[1:])):
        diff = b - a if increasing else a - b
        if not (1 <= diff <= 3):
            unsafe_indicies.add(i)
            unsafe_indicies.add(i + 1)

    return unsafe_indicies


def is_safe(report):
    increasing_unsafes = find_unsafes(report, True)
    decreasing_unsafes = find_unsafes(report, False)

    return not increasing_unsafes or not decreasing_unsafes


def can_make_safe(report):
    increasing_unsafes = find_unsafes(report, True)
    decreasing_unsafes = find_unsafes(report, False)

    if not increasing_unsafes or not decreasing_unsafes:
        return True

    for idx in increasing_unsafes | decreasing_unsafes:
        modified_report = report[:idx] + report[idx + 1 :]
        if is_safe(modified_report):
            return True

    return False


def main():
    inp = [l.strip() for l in sys.stdin.readlines()]

    safe_count = 0
    can_make_safe_count = 0
    for report in inp:
        report = [int(x) for x in report.split()]
        if is_safe(report):
            safe_count += 1
        if can_make_safe(report):
            can_make_safe_count += 1

    print(safe_count)
    print(can_make_safe_count)


if __name__ == '__main__':
    main()
