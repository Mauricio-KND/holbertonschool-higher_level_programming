#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if str is ord(c) >= 'a' and ord(c) <= 'z':
            str = char(ord(c - 32))
            print(str)
