import praw
import pdb
import re
import os
from typing import List
from lxml import html
import requests
from bs4 import BeautifulSoup

# Utility functions for controlling the storage and arrays associated with it


# returns an array of each string in posts_replied_to.txt, which is all the post id's previously replied to
def get_posts_array() -> List[str]:
    if not os.path.isfile("storage\posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("storage\posts_replied_to.txt", "r") as f:
           posts_replied_to = f.read()
           posts_replied_to = posts_replied_to.split("\n")
           posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to


# takes an array of strings of post id, wirtes them to the posts_replied_to.txt
def store_posts(posts_replied_to: List[str]) -> None:
    with open("storage\posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


# returns an array of each string in comments_replied_to.txt, which is all the comment id's previously replied to
def get_comments_array() -> List[str]:
    if not os.path.isfile("storage\comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("storage\comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    return comments_replied_to


# takes an array of strings of comments id, writes them to the comments_replied_to.txt
def store_comments(comments_replied_to: List[str]) -> None:
    with open("storage\comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")


# if the array of submissions gets too big, will cut down to save on space
# and computing time.  Will likely increase this if the bot goes into production,
# but for now, just testing.
def clean_replied_to_array(text: List[str]) -> List[str]:
    if len(text) >= 10000:         # if the array has more than 10000 things in it, cut it by half
        new_len = int(len(text)/2)
        new_text = []
        for x in range(new_len, len(text)-1):
            new_text.append(text[x])
        return new_text
    else:                       # if not, just return what was given
        return text
