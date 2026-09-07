#!/usr/bin/python3
"""This module defines a MyList class that extends list."""


class MyList(list):
    """A list subclass with a method to print sorted contents."""

    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        print(sorted(self))
