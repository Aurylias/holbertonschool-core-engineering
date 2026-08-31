#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            print(f"{char}".format(), end="")
        else:
            print(f"{chr(ord(char) - 32)}".format(), end="")
