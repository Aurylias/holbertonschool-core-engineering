#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            print(char, end="")
        else:
            print(chr(ord(char) - 32), end="")
