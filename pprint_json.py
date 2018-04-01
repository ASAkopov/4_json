# -*-coding:utf-8-*-

import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as file_object:
        json_object = json.load(file_object)
    return json_object


def pretty_print_json(data):
    print(json.dumps(
        data,
        ensure_ascii=False,
        indent=4,
        sort_keys=True,
    ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            jsonobject = load_data(file_path)
        except IOError:
            print(u"Can not open file.")
        except ValueError:
            print(
                u"""Impossiple to deserialize JSON. 
                Possible inconsistency with format."""
            )
        else:
            pretty_print_json(jsonobject)
    else:
        print(u"Filepath was not specified.")
