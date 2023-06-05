import unittest
from src.main.python.python_oas_validator import extract_text_between_quotes, validate_local_spec


class test_python_oas_validator(unittest.TestCase):
    def test_extract_text_between_quotes_valid_input_single_quotes(self):
        text = "This is 'some' text"
        result = extract_text_between_quotes(text)
        self.assertEqual(result, "some")

    def test_extract_text_between_quotes_valid_input_multiple_quotes(self):
        text = "This is 'some' text with 'multiple' quotes"
        result = extract_text_between_quotes(text)
        self.assertEqual(result, "some")

    def test_extract_text_between_quotes_no_quotes(self):
        text = "This is some text"
        result = extract_text_between_quotes(text)
        self.assertIsNone(result)

    def test_extract_text_between_quotes_invalid_input(self):
        text = 123
        result = extract_text_between_quotes(text)
        self.assertIsNone(result)

    def test_validate_local_spec_valid_yaml_file(self):
        spec_file_path = "resources/oas_/spec.yaml"
        validation_errors = []
        show_detailed_messages = False
        result = validate_local_spec(spec_file_path, validation_errors, show_detailed_messages)
        self.assertTrue(len(result) == 0)

    def test_validate_local_spec_valid_json_file(self):
        spec_file_path = "resources/oas_/spec.json"
        validation_errors = []
        show_detailed_messages = False
        result = validate_local_spec(spec_file_path, validation_errors, show_detailed_messages)
        self.assertTrue(len(result) == 0)

    def test_validate_local_spec_invalid_yaml_file(self):
        local_spec_file = "resources/oas_/spec_error.yaml"
        show_detailed_messages = False
        result = validate_local_spec(local_spec_file, [], show_detailed_messages)
        self.assertTrue(len(result) > 0)

    def test_validate_local_spec_invalid_file_extension_yaml(self):
        spec_file_path = "resources/oas_/spec.txt"
        validation_errors = []
        show_detailed_messages = False
        result = validate_local_spec(spec_file_path, validation_errors, show_detailed_messages)
        self.assertTrue(result)

    def test_validate_local_spec_unsupported_version_yml(self):
        spec_file_path = "resources/oas_/spec_310.yaml"
        validation_errors = []
        show_detailed_messages = False
        result = validate_local_spec(spec_file_path, validation_errors, show_detailed_messages)
        self.assertFalse(result)

    if __name__ == '__main__':
        unittest.main()
