#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    """Safely print a list"""
    total = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            total += 1
    except:
        print("Given lenght is bigger than the len of the list")
    print("")
    return total
