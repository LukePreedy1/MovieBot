import praw
import pdb
import re
import os
from lxml import html
import requests
from bs4 import BeautifulSoup

def get_posts_array():
    if not os.path.isfile("storage\posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("storage\posts_replied_to.txt", "r") as f:
           posts_replied_to = f.read()
           posts_replied_to = posts_replied_to.split("\n")
           posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to

def get_comments_array():
    if not os.path.isfile("storage\comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("storage\comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    return comments_replied_to

def store_posts(posts_replied_to):
    with open("storage\posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

def store_comments(comments_replied_to):
    with open("storage\comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")


# String -> String
# takes in the name of a movie, returns the imdb search address for it
def imdb_search_parser(movie_name):
    thing = movie_name.lower()
    thing = thing.replace(" ", "+")
    formatted = "http://www.imdb.com/find?ref_=nv_sr_fn&q="
    formatted += thing
    formatted += "&s=all"
    return formatted

# String -> String
# takes a string of text from a post or comment, then parses the movie title from it
# the movie title will be in the format: {title}
def parse_movie_title(text):
    title = text[text.find("{")+1: ]
    title = title[ :title.find("}")]
    return title

# String -> String
# takes a string of the title of a movie, then formats a reply to it's imdb page
def imdb_reply_format(title):
    url = imdb_url_finder(imdb_search_parser(title))
    response = "["
    response += title
    response += "]("
    response += url
    response += ")"
    return response

# String -> String
# takes in a string of the url of the search page of the movie, then returns the imdb page of the movie
def imdb_url_finder(search_url):
    page = requests.get(search_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('td', class_='result_text')

    title = results[0]
    tag = title.a
    url = "http://www.imdb.com"
    url += tag['href']
    return url
