#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
absNumber = -number if number < 0 else number
neg = True if number < 0 else False
digit = absNumber % 10
if digit > 5:
    if neg:
        print(f"Last digit of {number} is -{digit} and is greater than 5")
    else:
        print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit < 6 and digit != 0:
    if neg:
        print(f"Last digit of {number} is -{digit}\
              and is less than 6 and not zero")
    else:
        print(f"Last digit of {number} is {digit}\
              and is less than 6 and not zero")
else:
    print(f"Last digit of {number} is {digit} and is zero")
