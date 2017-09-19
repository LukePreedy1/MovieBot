import praw
import pdb
import re
import os
from lxml import html
import requests

reddit = praw.Reddit('bot1')

#TODO change this when the bot is complete
subreddit = reddit.subreddit('moviebottestingarena')

if not os.path.isfile("storage\posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("storage\posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

#  TODO Will get HTML from a webpage.  will update later to get any webpage
#  page = requests.get('www.imdb.com')
#  tree = html.fromstring(page.content)


if not os.path.isfile("storage\comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("storage\comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("test", submission.selftext, re.IGNORECASE):
            submission.reply("The test was successful")
            posts_replied_to.append(submission.id)
    for top_level_comment in submission.comments:
        if re.search("successful", top_level_comment.body, re.IGNORECASE) and top_level_comment.id not in comments_replied_to:
            top_level_comment.reply("I'm glad that it went so well")
            comments_replied_to.append(top_level_comment.id)
    print(submission.title)
    print(submission.selftext)
    print(submission.author)
    print(submission.score)
    print("---------------------------------------\n")

with open("storage\posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

with open("storage\comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")
