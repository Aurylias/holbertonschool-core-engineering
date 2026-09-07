#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    indexErr = True
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            total += 1
        except (ValueError, TypeError) as e:
            pass
        except IndexError:
            if indexErr:
                print("Traceback (most recent call last):", end="")
                indexErr = False
    print("")
    return total
