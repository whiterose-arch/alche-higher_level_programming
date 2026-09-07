#!/usr/bin/python3
"""Defines safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list that are integers."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
