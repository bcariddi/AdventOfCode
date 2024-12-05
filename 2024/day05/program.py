#!/usr/bin/env python3

import sys
from pprint import pprint
from collections import defaultdict
from functools import cmp_to_key


def make_rules_dict(rules):
    rules_dict = defaultdict(set)
    for rule in rules:
        first, second = map(int, rule.split('|'))
        rules_dict[first].add(second)

    return rules_dict


def is_order_valid(order, rules_dict):
    seen = set()
    for e in order:
        if seen.intersection(rules_dict[e]):
            return False
        seen.add(e)

    return True


def find_middle_value(order):
    return order[(len(order) - 1) // 2]


def compare(a, b, rules_dict):
    if a in rules_dict[b]:
        return -1
    elif b in rules_dict[a]:
        return 1
    return 0


def reorder(order, rules_dict):
    order.sort(key=cmp_to_key(lambda x, y: compare(x, y, rules_dict)))


def process_orders(orders, rules_dict):
    total = 0
    reordered_total = 0

    for order_str in orders:
        order = [int(x) for x in order_str.split(',')]
        if is_order_valid(order, rules_dict):
            total += find_middle_value(order)
        else:
            reorder(order, rules_dict)
            reordered_total += find_middle_value(order)

    return total, reordered_total


def parse_input():
    inp = [l.strip() for l in sys.stdin.readlines()]
    split = inp.index('')
    return inp[:split], inp[split + 1 :]


def main():
    rules, orders = parse_input()

    rules_dict = make_rules_dict(rules)

    total, reordered_total = process_orders(orders, rules_dict)

    print(total)
    print(reordered_total)


if __name__ == '__main__':
    main()
