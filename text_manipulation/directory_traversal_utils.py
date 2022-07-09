import os

from yaml_to_json_file_utils import get_dict_object_from_yaml_file, write_yaml_dict_to_json_file, delete_file


def convert_all_yaml_to_json_in_dir(root_dir: str) -> None:
    for directory_name, sub_dir_name, file_list in os.walk(root_dir):
        for file_name in file_list:
            pass
            # TODO: Convert file to json if it is yaml
            # TODO: Delete the yaml file


if __name__ == '__main__':
    convert_all_yaml_to_json_in_dir("./test_directory")
