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

def update_movie_in_database(movie_url: str):
    cnx = mysql.connector.connect(user='LukePreedy', password='Yourface1234', hose='127.0.0.1', database='moviebot_thing')
    cursor = cnx.cursor
    query = (
        "SELECT movie AS e "
        "WHERE movie_imdb_url = {0}".format(movie_url))
    cursor.execute(query)
    #for url in cursor:
#        print("The url is {0}\n".format(url))


def add_movie_to_table(movie_true_title: str, cnx):
    thing


def increment_number_of_references(movie_true_title: str, cnx):
    thing
