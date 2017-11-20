import praw
import pdb
import re
import os
from typing import List
from lxml import html
from utils.submission_utils import reply_format_movie_not_exist
from utils.storage_utils import *
import requests
from bs4 import BeautifulSoup

# Utility functions that are only used for working with IMDB

# takes a string of the title of a movie, then formats a reply to it's imdb page
def imdb_reply_format(title: str) -> str:
    #url = imdb_url_finder(imdb_search_parser(title), title)
    url = imdb_url_finder(imdb_movie_search_parser(title), title)

    if url == "":
        return reply_format_movie_not_exist(title)

    score = imdb_url_score_getter(url)
    response= ""
    true_title = imdb_url_name_getter(url)
    if score != -1:
        response += "[{0}]({1}) has an imdb score of {2}".format(true_title, url, score)
    else:                                           # if the movie has no score,
        response += "[{0}]({1})".format(true_title,url)  # I assume that it just hasn't come out yet,
                                                    # and so will just give the name and link, no score
    return response


# takes in the name of a movie, returns the imdb search address for a movie
# with the exact same name.  Explicitly, a movie, no exceptions.
# Will be good for troubleshooting
def imdb_movie_exact_search_parser(movie_name: str) -> str:
    thing = movie_name.lower()
    this = thing.replace(" ", "%20")
    formatted = "http://www.imdb.com/find?q="
    formatted += thing
    formatted += "&s=tt&ttype=ft&exact=true&ref_=fn_tt_ex"
    return formatted


# takes in the name of a movie, returns the imdb search address for exclusively looking for movies
def imdb_movie_search_parser(movie_name: str) -> str:
    thing = movie_name.lower()
    thing.replace(" ", "%20")
    formatted = "http://www.imdb.com/find?q="
    formatted += thing
    formatted += "&s=tt&ttype=ft&ref_=fn_ft"
    return formatted


# takes in the name of a movie, returns the imdb search address for it
def imdb_search_parser(movie_name: str) -> str:
    thing = movie_name.lower()
    thing = thing.replace(" ", "+")
    formatted = "http://www.imdb.com/find?ref_=nv_sr_fn&q="
    formatted += thing
    formatted += "&s=all"
    return formatted


# takes in a string of the url of the page of the movie, then returns the name of the movie that the page is of
def imdb_url_name_getter(page_url: str) -> str:
    page = requests.get(page_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('h1', class_='')
    title = results[0].text
    title = title[:len(title)-1]
    return title


# takes in a string of the url of the search page of the movie, then returns the imdb page of the movie
def imdb_url_finder(search_url: str, name: str) -> str:
    page = requests.get(search_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('td', class_='result_text')

    # Will check all the results on the page
    for x in range(0, len(results)):
        # if the name being checked is equal to to the name we are looking for
        # TODO if there are problems later from going to the wrong url, becuase it contains
        #      a substring that is similar to the given title, then this is likely the issue
        if results[x].a.text.lower() in str(name).lower() or str(name).lower() in results[x].a.text.lower():
            tag = results[x].a
            url = "http://www.imdb.com"
            url += tag['href']
            # then we return the correct url
            return url
    return ""


# takes in a string of the url of the page of a movie, then returns the score that it received as a float
def imdb_url_score_getter(page_url: str) -> float:
    try:
        page = requests.get(page_url)

        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find('div', class_='ratingValue')

        score = result.strong.span.text

        return float(score)   # converts the score into a float

    except AttributeError:
        print("AttributeError.  This is happening because the movie does not have a score.\n")
        return float(-1)


# takes in a string for a movie title, then returns whether or not it exists
# TODO make this work.  It currently just causes an IndexError if the movie does not exist,
#      I want to make it actually do what it is supposed to do.  It works for now, just fix later
def imdb_does_movie_exist(movie_title: str) -> bool:
    search_url = imdb_search_parser(movie_title)
    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('div', class_='findNoResults')
    return True
