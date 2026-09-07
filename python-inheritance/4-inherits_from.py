#!/usr/bin/python3
"""This module defines a function that checks inherited class membership."""


def inherits_from(obj, a_class):
    """Return True if obj inherits (directly or indirectly) a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
