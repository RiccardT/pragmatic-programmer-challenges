import json
import os

from ruamel.yaml import YAML


def get_dict_object_from_yaml_file(file_name: str) -> dict:
    with open(file_name, 'r') as yaml_file:
        yaml_string = yaml_file.read()
        yaml_loader = YAML(typ='safe')
        return yaml_loader.load(yaml_string)


def write_yaml_dict_to_json_file(yaml_dict: dict, file_path: str) -> None:
    """
    Writes a parsed yaml data dictionary to a filepath.

    :param yaml_dict: The dictionary containing the parsed yaml data you wish to convert to JSON
    :param file_path: the full relative or absolute file name you wish to create. The function will add the ".json suffix for you
    :return: None
    """
    assert(type(yaml_dict) == dict)
    with open(file_path + '.json', 'w') as json_file:
        json.dump(yaml_dict, json_file, indent=2)


def delete_file(file_path: str) -> None:
    try:
        os.remove(file_path)
    except OSError as os_error:
        print("Error: %s - %s." % (os_error.filename, os_error.strerror))
