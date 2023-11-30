#!/usr/bin/env python3

import sys
import re


def find_regex(rules, n=0):
    if n == 8:
        return find_regex(rules, 42) + '+'
    elif n == 11:
        a = find_regex(rules, 42)
        b = find_regex(rules, 31)
        return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

    rule = rules[n]

    if rule.startswith('"'):
        return rule.strip('"')
    else:
        options = rule.split(' | ')
        chunk = []
        for option in options:
            nums = [int(x) for x in option.split(' ')]
            chunk.append(''.join(find_regex(rules, num) for num in nums))
        return '(?:' + '|'.join(chunk) + ')'


def main():
    text = sys.stdin.read().splitlines()
    split_i = text.index('')
    rules_text, messages_text = text[:split_i], text[split_i+1:]

    rules = {}
    for r in rules_text:
        key, val = [x.strip() for x in r.split(':')]
        rules[int(key)] = val

    reg = find_regex(rules)
    count = 0
    for message in messages_text:
        if re.fullmatch(reg, message):
            count += 1

    print(count)


if __name__ == '__main__':
    main()