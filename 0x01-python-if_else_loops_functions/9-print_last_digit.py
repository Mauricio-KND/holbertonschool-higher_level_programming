#!/usr/bin/python3
def print_last_digit(number):
    LstDgt = abs(number) % 10
    print('{}'.format(LstDgt), end='')
    return LstDgt
