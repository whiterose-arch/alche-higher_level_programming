#!/usr/bin/python3

"""
Returns the dictionary description with simple data structure
for JSON serialization of an object.
Args:
    obj (object): The object to convert to a dictionary.
Returns:
    dict: The dictionary description of the object.
"""

def class_to_json(obj):
  return obj.__dict__
