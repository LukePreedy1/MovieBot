import praw
import pdb
import re
import os
from lxml import html
import utils
from responses import format_response_test, response_test, movie_response_test
import requests
from bs4 import BeautifulSoup

reddit = praw.Reddit('bot1')

#TODO change this when the bot is complete
subreddit = reddit.subreddit('moviebottestingarena')

format_response_test(subreddit, 5)
response_test(subreddit, 5)
movie_response_test(subreddit, 5)
