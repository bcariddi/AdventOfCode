#!/usr/bin/env python3

import sys
import re


def find_matches_simple(string):
    regex = r"mul\([0-9]+,[0-9]+\)"
    return re.findall(regex, string)


def find_matches_complex(string):
    regex = r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)"
    return re.findall(regex, string)


def process_matches(matches):
    line_total = 0
    do_state = True
    for match in matches:
        if match == "don't()":
            do_state = False
            continue
        elif match == "do()":
            do_state = True
            continue

        if do_state:
            n1, n2 = [int(x) for x in match.split("(")[1].strip(")").split(",")]
            line_total += n1 * n2

    return line_total


def main():
    inp = [l.strip() for l in sys.stdin.readlines()]
    string = ""
    for line in inp:
        string += line

    matches = find_matches_simple(string)
    print(process_matches(matches))

    matches = find_matches_complex(string)
    print(process_matches(matches))


if __name__ == "__main__":
    main()
