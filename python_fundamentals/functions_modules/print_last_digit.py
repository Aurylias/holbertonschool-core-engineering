#!/usr/bin/env python3
def print_last_digit(number):
    """Print the last digit of a number"""
    number = -number if number < 0 else number
    digit = number % 10
    print(digit)
    return digit