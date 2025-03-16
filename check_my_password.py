import requests
import hashlib


def request_api_data(query_char):
    '''fetched data from the API using the first 5 characters of the hashed password'''
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the API and try again")
    return response


def read_res(response):
    '''Read the response from the API'''
    print(response.text)


def pwned_api_check(password):
    '''Check if the password exists in the API response'''
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    return response
