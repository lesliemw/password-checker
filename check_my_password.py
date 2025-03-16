import requests

url = "https://api.pwnedpasswords.com/range/" + \
    "70B64"
response = requests.get(url)
print(response.text)
