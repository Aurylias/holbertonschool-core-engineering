#!/usr/bin/env python3
"""Module that extend python lists"""


class VerboseList(list):
    """A list that print the element that as been added or removed"""
    def append(self, item):
        """Add the specified item at the end of the list"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Add the specified iterable at the end of the list"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove the specified item from the  list"""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, value=None):
        """Remove the item at the specified index from the list"""
        if value is None:
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
            return item
        else:
            item = super().pop(value)
            print("Popped [{}] from the list.".format(item))
            return item
