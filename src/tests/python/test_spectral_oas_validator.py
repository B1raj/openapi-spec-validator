import unittest
from src.main.python.spectral_oas_validator import validate_local_spec


class test_spectral_oas_validator(unittest.TestCase):

    def test_validate_local_spec_valid_yaml_file(self):
        spec_file_path = "resources/oas_/spec.yaml"
        validation_errors = []
        result = validate_local_spec(spec_file_path, validation_errors)
        self.assertTrue(result)

    def test_validate_local_spec_invalid_yaml_file(self):
        local_spec_file = "resources/oas_/spec_error.yaml"
        result = validate_local_spec(local_spec_file, [])
        self.assertFalse(result)

    def test_validate_local_spec_invalid_file_extension_yaml(self):
        spec_file_path = "resources/oas_/spec.txt"
        validation_errors = []
        result = validate_local_spec(spec_file_path, validation_errors)
        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()
