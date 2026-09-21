#!/usr/bin/env python3
"""Module for printing files"""


def read_file(filename=""):
    """Print a whole file"""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip('\n'))
