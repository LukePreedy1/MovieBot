import praw
import pdb
import re
import os
from utils import *
from lxml import html
from responses import *
import requests
from bs4 import BeautifulSoup
from database_control import *

reddit = praw.Reddit('bot1')

#TODO change this when the bot is complete
subreddit = reddit.subreddit('moviebottestingarena')

#TODO improvement ideas:
#  Also, maybe change to movies are in {}, shows [], games <>, etc.
#  Could potentially make this generic, work for other formats too,
#  such as discord, but that will be much further down the line
movie_response_test(subreddit, 5)
