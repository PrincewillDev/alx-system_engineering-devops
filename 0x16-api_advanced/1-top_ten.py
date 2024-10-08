#!/usr/bin/python3
"""
This module contains a function that queries the Reddit
API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10
    hot posts listed for a given subreddit.
    Args:
        subreddit(str): Subreddit
    Return:
        None
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {"User-Agent": "0x16. API advanced (by Princewill_Fidelis)"}
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
