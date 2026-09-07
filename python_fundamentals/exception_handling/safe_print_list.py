#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    """Safely print a list"""
    try:
        for i in range(x):
            print(my_list[i], end="")
    except:
        print("Given lenght is bigger than the len of the list")
