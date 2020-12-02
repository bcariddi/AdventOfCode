#!/usr/bin/env python3

import sys

''' returns only pair of numbers in list l that sum to 2020 - O(n) time '''
def find_twosum(l):
    distance = {} # stores each number as the value of its complement (key)

    for n in l:
        comp = 2020 - n
        if n not in distance: # if n is not a key, add its complement and n as a key-value pair
            distance[comp] = n
        else: # if n is a key, return it and its complement
            return n, comp

''' returns only triplet of nubmers in list l that sum to 2020 - O(n^2) time '''
def find_threesum(l):
    length = len(l)

    for i in range(length - 1):
        seen = set() # stores numbers that have been seen to compute triple sums

        curr = 2020 - l[i]

        for j in range(i + 1, length):
            if curr - l[j] not in seen:
                seen.add(l[j])
            else:
                return l[i], l[j], curr - l[j]

def main():
    l = []
    for line in sys.stdin:
        l.append(int(line))
    
    n1, n2 = find_twosum(l)
    print('Two sum: ' + str(n1) + ' * ' + str(n2) + ' = ' + str(n1 * n2) + '\n')
    
    n3, n4, n5 = find_threesum(l)
    print('Three sum: ' + str(n3) + ' * ' + str(n4) +  ' * ' + str(n5) + ' = ' + str(n3 * n4 * n5))

if __name__ == '__main__':
    main()
