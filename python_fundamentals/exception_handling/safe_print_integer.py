#!/usr/bin/env python3
def safe_print_integer(value):
    try:
        if value.is_Integer():
            print(value)
        else:
            raise TypeError()
    except TypeError:
        return False
