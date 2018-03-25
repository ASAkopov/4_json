import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as fid:
        jsondata = json.load(fid)
    return jsondata

def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii = False, indent = 4, sort_keys = True))


if __name__ == '__main__':
    filepath = sys.argv[1]
    data = load_data(filepath)
    pretty_print_json(data)
