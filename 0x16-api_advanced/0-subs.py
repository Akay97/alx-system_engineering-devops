#!/usr/bin/python3
"""
This module contains a function to query the Reddit API and return the number of subscribers
for a given subreddit. If the subreddit is invalid, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if invalid.
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    return 0
