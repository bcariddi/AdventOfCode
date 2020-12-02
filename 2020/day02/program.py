#!/usr/bin/env python3

import sys

count1 = 0
count2 = 0

for line in sys.stdin:
    rule, letter, password = line.split()
    
    mini, maxi = map(int, rule.split('-'))
    letter = letter.strip(':')

    if password.count(letter) < mini or password.count(letter) > maxi:
        pass
    else:
        count1 += 1 

    if password[mini - 1] == letter:
        if password[maxi - 1] == letter:
            pass
        else:
            count2 += 1
    elif password[maxi - 1] == letter:
        if password[mini - 1] == letter:
            pass
        else:
            count2 += 1


print(count1)
print(count2)
