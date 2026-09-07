#!/usr/bin/python3
"""Defines safe_print_integer."""


def safe_print_integer(value):
    """Print value as an integer, return True if it worked."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
