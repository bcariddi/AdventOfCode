#!/usr/bin/env python3

import sys
import itertools as it
from collections import Counter


def main():
    text = sys.stdin.read().splitlines()

    all_foods = set()
    times = Counter()
    pos = {}

    for line in text:
        a, b = line.split(" (contains ")
        foods = set(a.split())
        algs = set(b[:-1].split(", "))

        all_foods |= foods
        times.update(foods)

        for alg in algs:
            if alg not in pos:
                pos[alg] = foods.copy()
            else:
                pos[alg] &= foods

    bad = set(it.chain.from_iterable(pos.values()))

    print(sum(times[food] for food in (all_foods - bad)))

    taken = set()
    items = []
    while True:
        for alg, foods in pos.items():
            if len(foods - taken) == 1:
                o = min(foods - taken)
                items.append((alg, o))
                taken.add(o)
                break
        else:
            break

    print(",".join(x[1] for x in sorted(items)))


if __name__ == '__main__':
    main()