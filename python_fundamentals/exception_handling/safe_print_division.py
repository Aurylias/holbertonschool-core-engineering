#!/usr/bin/env python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except ArithmeticError as e:
        print("Inside result: None")
    finally:
        try:
            print("Inside result: {}".format(a / b))
        except ZeroDivisionError:
            pass
    return None
