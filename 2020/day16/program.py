#!/usr/bin/env python3

import sys


def find_valid(rules, ticket):
    for num in ticket:
        num_valid = False
        for field in rules:
            if num in rules[field]:
                num_valid = True

        if not num_valid:
            return num

    return -1


def main():
    # input parsing fun
    text = sys.stdin.read().splitlines()

    rules = {}
    i = 0
    while not text[i].startswith('your'):
        field, rule_text = text[i].split(':')
        first_rule, second_rule = rule_text.split(' or ')
        first_rule, second_rule = first_rule.strip(), second_rule.strip()
        first_low, first_up = [int(x) for x in first_rule.split('-')]
        second_low, second_up = [int(x) for x in second_rule.split('-')]

        rules[field] = set()
        for x in range(first_low, first_up + 1):
            rules[field].add(x)
        for x in range(second_low, second_up + 1):
            rules[field].add(x)
        i += 1

    i += 1
    your_ticket = [int(x) for x in text[i].split(',')]

    i += 2
    n_nearby = 0
    nearby_tickets = []
    while i < len(text):
        nearby_tickets.append([int(x) for x in text[i].split(',')])
        i += 1
        n_nearby += 1

    valid_tickets = [your_ticket]
    # Part 1
    invalid = 0
    for ticket in nearby_tickets:
        val = find_valid(rules, ticket)
        if val > -1:
            invalid += val
        else:
            valid_tickets.append(ticket)

    # print(invalid)

    # Part 2
    possibles = [set() for _ in your_ticket]

    for ticket in valid_tickets:
        for i, n in enumerate(ticket):
            possible = set()

            for field in rules:
                if n in rules[field]:
                    possible.add(field)

            if possible:
                possibles[i] = possibles[i].intersection(possible) if possibles[i] else possible

    possibles = sorted([[len(fields), i, fields] for i, fields in enumerate(possibles)])

    # stuck here


if __name__ == '__main__':
    main()