#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""
import sys

# Importing functions from previous files
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Load existing items if file exists, otherwise start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# 2. Add all arguments (excluding the script name itself) to the list
# sys.argv[1:] captures everything after 'python3 7-add_item.py'
items.extend(sys.argv[1:])

# 3. Save the updated list back to the file
save_to_json_file(items, filename)
