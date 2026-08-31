#!/usr/bin/env python3
def uppercase(str):
    finalString = ""
    for char in str:
        ascii = ord(char)
        if ascii >= 97 and ascii <= 122:
            finalString += chr(ascii - 32)
        else:
            finalString += char

    print("{}".format(finalString))
