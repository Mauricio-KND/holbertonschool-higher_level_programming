#!/usr/bin/python3
import sys
savefile = __import__('7-save_to_json_file').save_to_json_file
loadfile = __import__('8-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    try:
        List = loadfile("add_item.json")
    except:
        List = []
    for i in range(1, len(sys.argv)):
        List.append(sys.argv[i])
    savefile(List, "add_item.json")
