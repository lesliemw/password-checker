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


def get_password_leaks_count(hashes, hash_to_check):
    '''Read the number of times the password has been leaked'''
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    '''Check if the password exists in the API response'''
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(password):
    '''Main function to check the password using data collected from the API'''
    count = pwned_api_check(password)
    if count:
        print(
            f"{password} was found {count} times... you should probably change your password!")
    else:
        print(f"{password} was NOT found. Carry on!")
    return "done!"
