import praw
import pdb
import re
import os
from typing import List
from lxml import html
import requests
from bs4 import BeautifulSoup

# takes a string (submission selftext) returns an array of strings, titles to search for
def get_titles_array_from_submission(text: str) -> List[str]:
    titles = []
    index = 0
    while 1 :
        try:
            if text.find("{", index) >= 0 and text.find("}", index) > 0:
                title = parse_movie_title(text[index:])  #  gets the movie title, starting from index
                titles.append(title)
                dif = text.find("}", index)
                index += dif
            else:
                return titles
        except IndexError:
            print("Something Fucked up\n")


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


# takes an array of strings of post id, wirtes them to the posts_replied_to.txt
def store_posts(posts_replied_to: List[str]) -> None:
    with open("storage\posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


# takes an array of strings of comments id, writes them to the comments_replied_to.txt
def store_comments(comments_replied_to: List[str]) -> None:
    with open("storage\comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")


# takes in the name of a movie, returns the imdb search address for it
def imdb_search_parser(movie_name: str) -> str:
    thing = movie_name.lower()
    thing = thing.replace(" ", "+")
    formatted = "http://www.imdb.com/find?ref_=nv_sr_fn&q="
    formatted += thing
    formatted += "&s=all"
    return formatted

# takes a string of text from a post or comment, then parses the movie title from it
# the movie title will be in the format: {title}
def parse_movie_title(text: str) -> str:
    movie_title = text[text.find("{")+1: ]
    movie_title = movie_title[ :movie_title.find("}")]
    return movie_title

# takes a string of the title of a movie, then formats a reply to it's imdb page
def imdb_reply_format(title: str) -> str:
    url = imdb_url_finder(imdb_search_parser(title))
    #name = imdb_url_name_getter(url) TODO make this work
    response = "[{0}]({1})".format(title, url)

    return response


# takes in a string of the url of the search page of the movie, then returns the imdb page of the movie
def imdb_url_finder(search_url: str) -> str:
    page = requests.get(search_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('td', class_='result_text')

    title = results[0]
    tag = title.a
    url = "http://www.imdb.com"
    url += tag['href']
    return url


# takes in a string of the url of the page of the movie, then returns the name of the movie that the page is of
def imdb_url_name_getter(page_url: str) -> str:
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('h1', itemprop_='name') # TODO find the correct location and method to get this text
                                                    # TODO also use this to check that you are getting the correct name

    title = results[0].text
    print(title, "\n")
    return title


# takes in a string for a movie title, then returns whether or not it exists
def imdb_does_movie_exist(movie_title: str) -> bool:
    search_url = imdb_search_parser(movie_title)
    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('div', class_='findNoResults')
    return True
