import praw
import pdb
import re
import os
from utils import *
from lxml import html
from responses import *
import requests
from bs4 import BeautifulSoup

reddit = praw.Reddit('bot1')

#TODO change this when the bot is complete
subreddit = reddit.subreddit('moviebottestingarena')

#TODO improvement ideas:
#  to prevent linking to shitty parody names, check the scores of all
#  results, and return the highest scoring result.
#  Also, maybe change to movies are in {}, shows [], games <>, etc.
#  Could potentially make this generic, work for other formats too,
#  such as discord, but that will be much further down the line
movie_response_test(subreddit, 5)
