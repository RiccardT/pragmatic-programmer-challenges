import json
import os

from ruamel.yaml import YAML


def get_dict_object_from_yaml_file(file_name: str) -> dict:
    with open(file_name, 'r') as yaml_file:
        yaml_string = yaml_file.read()
        yaml_loader = YAML(typ='safe')
        return yaml_loader.load(yaml_string)


def write_yaml_dict_to_json_file(yaml_dict: dict, file_name: str) -> None:
    assert(type(yaml_dict) == dict)
    with open(file_name + '.json', 'w') as json_file:
        json.dump(yaml_dict, json_file, indent=2)


def delete_file(file_path: str) -> None:
    try:
        os.remove(file_path)
    except OSError as os_error:
        print("Error: %s - %s." % (os_error.filename, os_error.strerror))


# TODO: Create directory crawler
# TODO: Create command line interface
