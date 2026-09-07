#!/usr/bin/python3
"""This module defines a function that lists object attributes."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
