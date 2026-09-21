#!/usr/bin/env python3
"""Module to append text in a file"""


def append_write(filename="", text=""):
    """Append text a the end of a file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
