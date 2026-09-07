#!/usr/bin/python3
"""Defines safe_print_list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of my_list, catching out-of-range access."""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except (IndexError, TypeError):
        pass
    print()
    return count