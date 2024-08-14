#!/usr/bin/env python3

"""
This module contains a function that queries the Reddit
API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    if type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "0x16. API advanced (Princewill_Fidelis)"}
    response = requests.get(url, headers=header, allow_redirects=False)
    try:
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0

    except Exception as e:
        return 0