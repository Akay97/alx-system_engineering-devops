#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API and return a list of all hot article titles
for a given subreddit. If no results are found or the subreddit is invalid, the function returns None.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to return a list of titles of all hot articles for a given subreddit.
    If the subreddit is invalid, return None.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate the titles of hot articles (used for recursion).

    Returns:
        list: A list of hot article titles or None if the subreddit is invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom-User-Agent'}
    response = requests.get(url, headers=headers, params={'after': hot_list[-1] if hot_list else None}, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)

        # Check if there is a next page
        after = data.get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
