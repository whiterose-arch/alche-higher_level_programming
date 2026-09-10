#!/usr/bin/python3

import os
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

def add_item(args):
  my_list = load_from_json_file("add_item.json") if os.path.exists("add_item.json") else []
  my_list.extend(args)
  save_to_json_file(my_list, "add_item.json")

if __name__ == "__main__":
  add_item(sys.argv[1:])
  