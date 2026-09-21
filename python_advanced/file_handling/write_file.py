#!/usr/bin/env python3
"""Module for writing in file"""


def write_file(filename="", text=""):
    """Write a line in a file and create it if it doesn't exist"""
    with open(filename, "x", encoding="utf-8") as file:
        file.write(text)
