#!/usr/bin/env python3
def pow(a, b):
    """Raise a to the power of b"""
    result = a
    for num in range(1, b):
        result *= a
    return result
