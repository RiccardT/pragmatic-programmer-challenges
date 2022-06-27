import unittest
import os

from yaml_to_json_file_utils import get_dict_object_from_yaml_file, write_yaml_dict_to_json_file


class TestYamlFunctions(unittest.TestCase):

    test_yaml_file_path = './test_files/test.yaml'
    expected_json_file_path = './test_files/expected_json.json'
    actual_json_file_path = './test_files/actual_json.json'
    test_yaml_dict = {
            'doe': 'a deer, a female deer',
            'ray': 'a drop of golden sun',
            'pi': 3.14159,
            'xmas': True,
            'french-hens': 3,
            'calling-birds': ['huey', 'dewey', 'louie', 'fred']
        }

    def test_yaml_loader(self):
        actual_dict = get_dict_object_from_yaml_file(self.test_yaml_file_path)

        self.assertEqual(self.test_yaml_dict, actual_dict)

    def test_conversion_write_to_json(self):
        write_yaml_dict_to_json_file(self.test_yaml_dict, 'test_files/actual_json')
        with open(self.expected_json_file_path, 'r') as expected_json_file, \
                open(self.actual_json_file_path, 'r') as actual_json_file:
            expected_json_string = expected_json_file.read()
            actual_json_string = actual_json_file.read()
            self.assertEqual(expected_json_string, actual_json_string)


if __name__ == '__main__':
    unittest.main()
