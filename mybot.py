import praw
import pdb
import re
import os
from lxml import html
import utils
from responses import *
import requests
from bs4 import BeautifulSoup

reddit = praw.Reddit('bot1')

#TODO change this when the bot is complete
subreddit = reddit.subreddit('moviebottestingarena')

#format_response_test(subreddit, 5)
#response_test(subreddit, 5)

#TODO improvement idea:
#  to prevent linking to shitty parody names, check the scores of all
#  results, and return the highest scoring result.
#  Also, maybe change to movies are in {}, shows [], games <>, etc.
#  Could potentially make this generic, work for other formats too
movie_response_test(subreddit, 5)
