import sys
import json


def load_data(filepath):
    with open(filepath, "r") as file_object:
        python_object = json.load(file_object)
    return python_object


def pretty_print_json(object_to_print):
    print(json.dumps(
        object_to_print,
        ensure_ascii=False,
        indent=4,
        sort_keys=True,
    ))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Filepath was not specified.")
    file_path = sys.argv[1]
    try:
        python_object = load_data(file_path)
    except IOError:
        print("Can not open file.")
    except ValueError:
        print(
            "Impossiple to deserialize JSON. "
            "Possible inconsistency with format."
            )
    else:
        pretty_print_json(python_object)
