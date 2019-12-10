#!/usr/bin/python3
for first in range(10):
    for second in range(10):
        if first is 8 and second is 9:
            print('{:d}{:d}'.format(first, second))
        elif first < second:
            print('{:d}{:d}'.format(first, second), end=', ')
