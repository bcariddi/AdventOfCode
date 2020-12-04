#!/usr/bin/env python3 

import sys
import re

text = sys.stdin.readlines()

valid1 = 0
valid2 = 0

curr = ''
for line in text:
    if line != '\n': # adding lines to new passport
        curr += line

    else: # we have a complete passport, now check if it's valid
        fields = {'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'}
        if all(x in curr for x in fields):
            valid1 += 1
            tokens = curr.split()
            passport = True
            for token in tokens:
                key, value = token.split(':')

                if key == 'byr':
                    if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                        passport = False
                        break
                elif key == 'iyr':
                    if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                        passport = False
                        break
                elif key == 'eyr':
                    if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                        passport = False
                        break
                elif key == 'hgt':
                    if value.endswith('cm'):
                        loc = value.find('cm')
                        if int(value[:loc]) < 150 or int(value[:loc]) > 193:
                            passport = False
                            break
                    elif value.endswith('in'):
                        loc = value.find('in')
                        if int(value[:loc]) < 59 or int(value[:loc]) > 76:
                            passport = False
                            break
                    else:
                        passport = False
                        break
                elif key == 'hcl':
                    if not value.startswith('#'):
                        passport = False
                        break
                    else:
                        pattern = re.compile('#[a-f0-9]{6}')
                        if not pattern.fullmatch(value):
                            passport = False
                            break
                elif key == 'ecl':
                    ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                    if value not in ecls:
                        passport = False
                        break
                elif key == 'pid':
                    if len(value) != 9 or not value.isnumeric():
                        passport = False
                        break

            valid2 += passport

        curr = ''

print(valid1)
print(valid2)
