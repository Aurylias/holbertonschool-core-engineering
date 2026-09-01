#!/usr/bin/env python3
def pow(a, b):
    """Raise a to the power of b"""
    result = a
    for num in range(abs(b - 1)):
        if b > 0:
            print("in positive")
            result *= a
        else:
            print("in negative")
            result /= a
    return result
