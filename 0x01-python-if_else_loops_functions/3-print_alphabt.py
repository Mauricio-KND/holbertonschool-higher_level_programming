#!/usr/bin/python3
for number in range(97, 123):
    if number is 101 or number is 113:
        continue
    print('{:c}'.format(number), end="")
