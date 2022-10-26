#!/usr/bin/python3
"""Module which adds arguments to python file"""

import sys
import json
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []
json_file = 'add_item.json'


if os.path.exists(json_file) and os.path.getsize(json_file) > 0:
    my_list = load_from_json_file(json_file)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        my_list.append(arg)

save_to_json_file(my_list, json_file)
