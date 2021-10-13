#!/usr/bin/python3
'''script'''

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file1 = "add_item.json"
my_list = []

if os.path.isfile(file1):
    my_list = load_from_json_file(file1)

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, file1)
