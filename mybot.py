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

#  TODO Will get HTML from a webpage.  will update later to get any webpage
page = requests.get('http://www.imdb.com/find?ref_=nv_sr_fn&q=die+hard&s=all') # Example looking at search results for "Die Hard"

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('td', class_='result_text')

for title in results:
    tag = title.a
    print(tag['href'])  #  Will print out the imdb.com/ extension to get to the correct page!

#print(soup.prettify)

#print([type(item) for item in list(soup.children)])

tree = html.fromstring(page.content)
titles = tree.xpath('//body[@id="styleguide-v2"]/div[@id="wrapper"]/div[@id="root"]/div[@id="pagecontent"]/div[@id="content-2-wide"]/div[@id="main"]/div[@class="article"]/div[@class="findSection"]/table[@class="findList"]/tbody/tr[@class="findResult odd"]/td[@class="result_text"]/a[@href="/title/tt0095016/?ref_=fn_al_tt_1"]/text()')
#  titles = tree.xpath('//tbody/tr[@class="findResult odd"]/td[@class="result_text"]/a[@href="/title/tt0095016/?ref_=fn_al_tt_1"]/text()')
print("Name: ", titles)

format_response_test(subreddit, 5)
response_test(subreddit, 5)
movie_response_test(subreddit, 5)
