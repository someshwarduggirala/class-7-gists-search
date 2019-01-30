import requests
from pprint import pprint

BASE_URL = 'https://api.github.com/users/{username}/gists'


def get_gists(username):
    url = BASE_URL.format(username=username)
    resp = requests.get(url, params={'per_page': 100})
    if not resp.ok:
        return None
    return resp.json()

if __name__ == '__main__':
    gists = get_gists('gvanrossum')
    first_three_gists = gists[:3]

    for gist in first_three_gists:
        print("{:<40} | {}".format(gist['id'], gist['description']))