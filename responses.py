from utils import *
import utils
import praw
from praw.models import *
from utils.imdb_utils import *
from utils.storage_utils import *
from utils.submission_utils import *
import pdb
import re
import os
import mysql.connector

# responds to a post, then returns a boolean for if a response was made
def respond_to_post(submission):
    titles = get_titles_array_from_submission(submission.selftext) # returns an array of strings, all titles in brackets
    if re.search("{", submission.selftext, re.IGNORECASE):
        response = ""
        if len(titles) > 0:
            for title in titles:
                try:
                    if imdb_does_movie_exist(title):
                        response += imdb_reply_format(title)
                        response += "  \n"
                except IndexError:
                    print("The IndexError is happening because you are searching for something that doesn't exist\n")
                    response += reply_format_movie_not_exist(title)
                    response += "  \n"
            # Will only actually respond if there is something to respond with
            if len(response) > 0 :
                submission.reply(response)
                return True
    return False


# responds to all comments in a given submission, then returns an array of all
# comment ids that it responded to
def respond_to_comments(submission, comments_replied_to):
    coms = []
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments) :
            print("skipping this one, will add functionality later\n")
        elif re.search("{", top_level_comment.body, re.IGNORECASE) and top_level_comment.id not in comments_replied_to:
            titles = get_titles_array_from_submission(top_level_comment.body)
            response = ""
            if len(titles) > 0: # if there is at least one title to respond to:
                coms.append(top_level_comment.id)
                for title in titles:
                    try:
                        if imdb_does_movie_exist(title):
                            response += imdb_reply_format(title)
                            response += "  \n"
                    except IndexError:
                        print("The IndexError is happening because you are searching for something that doesn't exist\n")
                        response += reply_format_movie_not_exist(title)
                        response += "  \n"
                if len(response) > 0 and response != "":
                    top_level_comment.reply(response)
    return coms

# VOID
# the real meat of the project.  Will resopnd to a post or comment
# with the imdb link for the movie that is posted in format {name}
def movie_response_test(subreddit, num):
    num_posts_replied_to = 0
    num_comments_replied_to = 0
    coms = []

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    print("Movie Title Post Response Test")
    for submission in subreddit.hot(limit=num):
        if submission.id not in posts_replied_to:
            if (respond_to_post(submission)):
                posts_replied_to.append(submission.id)
                num_posts_replied_to += 1
        coms = respond_to_comments(submission, comments_replied_to)
        comments_replied_to += coms
        num_comments_replied_to += len(coms)
        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")
    print("Test replied to: ", num_posts_replied_to, " posts\n")
    print("test replied to: ", num_comments_replied_to, " comments\n")

    posts_replied_to = clean_replied_to_array(posts_replied_to)
    store_posts(posts_replied_to)

    comments_replied_to = clean_replied_to_array(comments_replied_to)
    store_comments(comments_replied_to)

    return
