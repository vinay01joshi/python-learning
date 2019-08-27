import requests
from vinpdf import pdf2text

response = requests.get("http://google.com")
print(response)
print(pdf2text.convert())
