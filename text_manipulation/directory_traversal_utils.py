import os

from yaml_to_json_file_utils import get_dict_object_from_yaml_file, write_yaml_dict_to_json_file, delete_file


def convert_all_yaml_to_json_in_dir(root_dir: str) -> None:
    for current_parent_dir, _, list_of_files_in_current_dir in os.walk(root_dir):
        for file_name in list_of_files_in_current_dir:
            if file_name.lower().endswith(".yaml"):
                yaml_file_path = os.path.join(current_parent_dir, file_name)
                replace_yaml_file_with_json_file(yaml_file_path)


def replace_yaml_file_with_json_file(yaml_file_path):
    yaml_dict: dict = get_dict_object_from_yaml_file(yaml_file_path)
    file_name_without_yaml_suffix = yaml_file_path.removesuffix(".yaml")
    write_yaml_dict_to_json_file(yaml_dict, file_name_without_yaml_suffix)
    delete_file(yaml_file_path)
