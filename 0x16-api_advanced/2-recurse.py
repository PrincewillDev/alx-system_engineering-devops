#!/usr/bin/python3
"""
This module contains a function that queries the Reddit
API and  returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ Returns a list containing the titles of all hot articles
    for a given subreddit.
    Args:
        subreddit(str): Subreddit
    Return:
        (list): List of hot articles or None on fail.
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    header = {"User-Agent": "0x16. API advanced (by Princewill_Fidelis)"}
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list)
            return hot_list
        else:
            return None
    except Exception as e:
        return None
