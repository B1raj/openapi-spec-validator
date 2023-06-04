# Openapi Specification Linter



 This code provides a convenient way to validate OpenAPI specification files and helps ensure that the specifications are accurate, compliant, and follow recommended practices. It supports better API development and documentation by catching errors and enforcing standards at an early stage.

## Spectral OAS

1. Install Spectral using the following command:
    - For Windows: [spectral.exe](https://github.com/stoplightio/spectral/releases/download/v6.7.0/spectral.exe)
    - For other platforms, follow the installation instructions on
      the [Spectral GitHub repository](https://github.com/stoplightio/spectral)

2. Extend default Spectral rules as needed or write your own rules.

3. Create a file named `.spectral.yaml` with the following content:
   ```yaml
   extends: ["spectral:oas", "spectral:asyncapi"]
   ```
4. Run spectral_oas_validator.py to validate your OpenAPI specifications.

## Python OpenAPI Spec Validator

1. Install openapi-spec-validator
   ```yaml
   pip install openapi-spec-validator
   ```
2. Run python_oas_validator.py to validate your OpenAPI specifications
   
