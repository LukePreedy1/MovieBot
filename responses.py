from utils import get_comments_array, get_posts_array, store_posts, store_comments, parse_movie_title, imdb_reply_format
import utils
import praw
import pdb
import re
import os

def format_response_test(subreddit, num):
    num_replied_to = 0
    response = ""

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    for submission in subreddit.hot(limit=num):
        if submission.id not in posts_replied_to:
            if re.search("format test", submission.selftext, re.IGNORECASE):
                response += ("[source](https://github.com/LukePreedy1/MovieBot)")
                submission.reply(response)
                posts_replied_to.append(submission.id)
                num_replied_to += 1

        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------\n")
    print("Formatted Response Test replied to:", num_replied_to, "\n")

    store_posts(posts_replied_to)
    store_comments(comments_replied_to)

    return

def response_test(subreddit, num):
    num_replied_to = 0

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    for submission in subreddit.hot(limit=num):
        if submission.id not in posts_replied_to:
            if re.search("test", submission.selftext, re.IGNORECASE):
                submission.reply("The test was successful")
                posts_replied_to.append(submission.id)
                num_replied_to += 1
        for top_level_comment in submission.comments:
            if re.search("successful", top_level_comment.body, re.IGNORECASE) and top_level_comment.id not in comments_replied_to:
                top_level_comment.reply("I'm glad that it went so well")
                comments_replied_to.append(top_level_comment.id)
                num_replied_to += 1
        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")
    print("Test replied to: ", num_replied_to, "\n")
    store_posts(posts_replied_to)
    store_comments(comments_replied_to)

    return


def movie_response_test(subreddit, num):
    num_replied_to = 0

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    for submission in subreddit.hot(limit=num):
        if submission.id not in posts_replied_to:
            if re.search("{", submission.selftext, re.IGNORECASE):
                title = parse_movie_title(submission.selftext)  #  the title of the movie
                submission.reply(imdb_reply_format(title))      #  formats the response
                posts_replied_to.append(submission.id)
                num_replied_to += 1
        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")
    print("Test replied to: ", num_replied_to, "\n")
    store_posts(posts_replied_to)
    store_comments(comments_replied_to)
    return
