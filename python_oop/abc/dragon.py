#!/usr/bin/env python3
"""Module for creating dragon"""


class SwimMixin:
    """Swim mixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Fly mixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon"""
    def roar(self):
        print("The dragon roars!")
