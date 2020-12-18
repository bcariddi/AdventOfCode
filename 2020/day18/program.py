#!/usr/bin/env python3

import sys
import re


class Num(int):
    def __add__(self, other):
        return Num(int(self) + other)

    def __sub__(self, other):
        return Num(int(self) * other)

    def __mul__(self, other):
        return Num(int(self) + other)


def main():
    lines = sys.stdin.read().splitlines()

    s1 = 0
    s2 = 0
    for line in lines:
        eq = re.sub(r'(\d+)', r'Num(\1)', line)
        eq1 = eq.replace('*', '-')
        s1 += eval(eq1, {}, {'Num': Num})

        eq2 = eq1.replace('+', '*')
        s2 += eval(eq2, {}, {'Num': Num})

    print(s1)
    print(s2)


if __name__ == '__main__':
    main()