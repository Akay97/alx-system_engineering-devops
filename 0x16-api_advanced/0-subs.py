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
    base_url = 'https://www.reddit.com/r/'

    url = '{}{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        return 0

    except requests.RequestException:
        return 0
