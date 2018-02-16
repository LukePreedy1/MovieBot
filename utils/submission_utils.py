import praw
from utils.imdb_utils import *
from utils.storage_utils import *
from praw.models import *
import pdb
import re
import os
from typing import List
from lxml import html
import requests
from bs4 import BeautifulSoup
import mysql.connector

# Utility functions for parsing submissions and comments

# takes a string (submission selftext) returns an array of strings, titles to search for
def get_titles_array_from_submission(text: str) -> List[str]:
    cnx = mysql.connector.connect(user='LukePreedy', password='Yourface1234', host='127.0.0.1', database='moviebot_thing')
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


# takes a string of text from a post or comment, then parses the movie title from it
# the movie title will be in the format: {title}
def parse_movie_title(text: str) -> str:
    movie_title = text[text.find("{")+1: ]
    movie_title = movie_title[ :movie_title.find("}")]
    return movie_title


# takes a string of the name of a movie, then formats a response for what to say
# if that movie does not exist, or cannot be found by the search
def reply_format_movie_not_exist(title: str) -> str:
    response = ""
    response += "Could not find a movie called **{0}**".format(title)
    return response
