import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as fid:
        json_data = json.load(fid)
    return json_data

def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii = False, indent = 4, sort_keys = True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    json_data = load_data(filepath)
    pretty_print_json(json_data)
