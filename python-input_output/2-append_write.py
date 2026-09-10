#!/usr/bin/python3

def append_write(filename="", text=""):
  with open(filename, "a", encoding="utf-8") as f:
    num_char = f.write(text)
    return num_char
    