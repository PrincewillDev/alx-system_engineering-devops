#!/usr/bin/env python3

"""
This module contains a function that queries the Reddit
API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
