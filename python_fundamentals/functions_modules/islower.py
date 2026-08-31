#!/usr/bin/env python3
def islower(c):
    """Check if a char is lowercase"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
