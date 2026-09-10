#!/usr/bin/python3

"""
Writes an object to a text file, using a JSON representation.
Args:
    my_obj (object): The object to write to the file.
    filename (str): The name of the file to write to.
Returns:
    None
"""
import json

def save_to_json_file(my_obj, filename):
  with open(filename, "w", encoding="utf-8") as f:
    json.dump(my_obj, f)
    