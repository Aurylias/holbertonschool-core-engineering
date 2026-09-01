#!/usr/bin/env python3
def pow(a, b):
    """Raise a to the power of b"""
    result = a
    for num in range(1, abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result

print(pow(-98, -10))
