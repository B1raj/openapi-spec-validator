import os
import re
import subprocess
from sys import platform


def validate_local_spec(spec_file_path, validation_errors):
    # Validate the local OpenAPI specification file using 'spectral lint' command

    # If not a YAML or YAML file, skip processing
    file_extension = os.path.splitext(spec_file_path)[1]
    if file_extension not in ['.yaml', '.yml']:
        print(f"Invalid file extension: {file_extension}. Skipping file: {spec_file_path}")
        return True

    command = f"spectral lint {spec_file_path}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()

    for error in output.decode().splitlines():
        validation_errors.append(error)

    # If errors are present, return False; otherwise, return True
    if validation_errors:
        num_errors = 0
        for error in validation_errors:
            print(f"{error}")
        match = re.search(r"\((\d+) errors,", validation_errors[-1])
        if match:
            num_errors = int(match.group(1))
        return num_errors <= 0


def print_usage():
    # Print usage information
    print("OpenAPI Specification Validator")
    print("Supported versions: 3.0.0 - 3.0.3, 2.0")
    print("Usage: python script_name.py <spec_file_or_directory>")
    print("Description: This program validates OpenAPI specification files.")
    print("             It supports OpenAPI versions 3.0.0 - 3.0.3 and 2.0.")
    print("             You can provide a single file or a directory containing multiple files.")
    print("             The program will validate each file and display any validation errors.")


def main(spec_file_or_directory):
    _separator = '/'
    if platform == "win32":
        _separator = '\\'

    path = spec_file_or_directory
    if os.path.isdir(path):
        print("Validating open API Specifications in the directory:")
        print(path)
        print("------------------------------")

        validation_result = True  # Initialize validation result as True

        for entry in os.scandir(path):
            if entry.is_file():
                result = validate_local_spec(entry.path, [])
                if not result:
                    validation_result = False  # Update validation result if any file validation fails

        return validation_result  # Return the final validation result
    else:
        return validate_local_spec(path, [])


if __name__ == "__main__":
    print_usage()
    print(main('./resources/oas_'))