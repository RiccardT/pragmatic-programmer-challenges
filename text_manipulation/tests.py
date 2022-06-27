import os.path
import unittest

from yaml_to_json_file_utils import get_dict_object_from_yaml_file, write_yaml_dict_to_json_file, delete_file


class TestYamlFunctions(unittest.TestCase):

    test_yaml_file_path = './test_files/test.yaml'
    expected_json_file_path = './test_files/expected_json.json'
    actual_json_file_path = './test_files/actual_json.json'

    def test_yaml_loader(self):
        expected_dict = {
            'doe': 'a deer, a female deer',
            'ray': 'a drop of golden sun',
            'pi': 3.14159,
            'xmas': True,
            'french-hens': 3,
            'calling-birds': ['huey', 'dewey', 'louie', 'fred']
        }

        actual_dict = get_dict_object_from_yaml_file(self.test_yaml_file_path)

        self.assertEqual(expected_dict, actual_dict)

    def test_conversion_write_to_json(self):
        write_yaml_dict_to_json_file({
            'doe': 'a deer, a female deer',
            'ray': 'a drop of golden sun',
            'pi': 3.14159,
            'xmas': True,
            'french-hens': 3,
            'calling-birds': ['huey', 'dewey', 'louie', 'fred']
        }, 'test_files/actual_json')

        with open(self.expected_json_file_path, 'r') as expected_json_file, \
                open(self.actual_json_file_path, 'r') as actual_json_file:
            expected_json_string = expected_json_file.read()
            actual_json_string = actual_json_file.read()

            self.assertEqual(expected_json_string, actual_json_string)

    def test_file_delete(self):
        path_to_file_to_be_deleted = "test_files/file_to_be_deleted.json"
        with open(path_to_file_to_be_deleted, 'w') as file_to_be_deleted:
            file_to_be_deleted.write("Ahhh I'm about to be destroyed!")

        delete_file(path_to_file_to_be_deleted)

        self.assertFalse(os.path.isfile(path_to_file_to_be_deleted))


if __name__ == '__main__':
    unittest.main()
