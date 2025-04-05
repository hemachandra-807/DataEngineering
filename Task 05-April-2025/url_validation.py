import re

url_validation = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(\/[^\s]*)?$"

url = "https://www.example.com/path/to/page"
match = re.fullmatch(url_validation, url)

if match:
    print("URL Validation is correct:", match.group())
else:
    print("URL is Invalid. Please enter a valid URL.")
