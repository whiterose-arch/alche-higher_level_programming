#!/usr/bin/python3

"""
Creates an Object from a “JSON file”
Args:
    filename (str): The name of the file to create the object from.
Returns:
    object: The object created from the JSON file.
"""

import json

def load_from_json_file(filename):
  with open(filename, "r", encoding="utf-8") as f:
    return json.load(f)
    