#!/usr/bin/python3
"""Reads a text file and prints it to stdout."""
def read_file(filename=""):
  with open(filename, encoding="utf-8") as f:
    result = f.read()
    print(result)
