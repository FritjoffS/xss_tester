# XSS Vulnerability Tester

## Description

This Python script is designed to test web applications for potential Cross-Site Scripting (XSS) vulnerabilities. It's intended for use in authorized bug bounty programs or on systems you have explicit permission to test.

## Features

- Automatically detects input fields on a given webpage
- Tests both GET and POST parameters
- Uses a customizable list of XSS payloads
- Supports loading payloads from an external file

## Prerequisites

- Python 3.9 or higher
- Conda (for environment management)

## Installation

1. Clone this repository or download the script files.

2. Navigate to the project directory:
    ```sh
    cd path/to/xss-tester
    ```

3. Create the Conda environment using the provided `environment.yml` file:
    ```sh
    conda env create -f environment.yml
    ```

4. Activate the Conda environment:
    ```sh
    conda activate xss-tester
    ```

## Usage

1. Ensure you have a `xss_payloads_list.txt` file in the same directory as the script. This file should contain XSS payloads, one per line.

2. Run the script:
    ```sh
    python xss_tester.py
    ```

3. Enter the target URL when prompted.

4. If no input fields are automatically detected, you'll be asked to manually enter parameter names.

5. The script will test each parameter with the provided XSS payloads and report potential vulnerabilities.

## Customizing Payloads

To use your own set of XSS payloads:

1. Edit the `xss_payloads_list.txt` file.
2. Add one payload per line.
3. Lines starting with '#' are treated as comments and ignored.

## Disclaimer

This tool is for educational and authorized testing purposes only. Always obtain explicit permission before testing any website or application for security vulnerabilities. Unauthorized testing may be illegal and unethical.

## Contributing

Contributions to improve the script are welcome. Please fork the repository and submit a pull request with your changes.

## License

MIT

## Author

FritjoFF

## Acknowledgments

- Thanks to the open-source community for various XSS payload lists and resources.
- This tool is intended for use in authorized bug bounty programs and security research.