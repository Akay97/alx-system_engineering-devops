#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and print the titles of the first 10 hot posts
listed for a given subreddit. If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/api/me.json"
    headers = {'User-Agent': 'Custom-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts[:10]:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
