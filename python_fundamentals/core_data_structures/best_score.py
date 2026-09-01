#!/usr/bin/env python3
def best_score(a_dictionary):
    bigKey = ""
    biggest = 0
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary[key]
            bigKey = key
    return bigKey
