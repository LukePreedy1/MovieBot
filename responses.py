from utils import *
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

    print("Formatted Post Response Test")
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

# VOID
# replies to posts and comments in the given subreddit, for the top INT num posts
# replies to generic test, will likely remove when in production
def response_test(subreddit, num):
    num_replied_to = 0

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    print("Generic Post Response Test")
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

# VOID
# the real meat of the project.  Will resopnd to a post or comment
# with the imdb link for the movie that is posted in format {name}
def movie_response_test(subreddit, num):
    num_posts_replied_to = 0
    num_comments_replied_to = 0

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    print("Movie Title Post Response Test")
    for submission in subreddit.hot(limit=num):
        if submission.id not in posts_replied_to:
            titles = get_titles_array_from_submission(submission.selftext) # returns an array of strings, all titles in brackets
            if re.search("{", submission.selftext, re.IGNORECASE):
                try:
                    response = ""
                    if len(titles) > 0:
                        posts_replied_to.append(submission.id)
                        num_posts_replied_to += 1
                        for title in titles:
                            response += imdb_reply_format(title)
                            response += "  \n"
                        submission.reply(response)
                except IndexError:
                    print("something fucked up\n")
        print("Movie Title Comment Response Test")
        for top_level_comment in submission.comments:
            if re.search("{", top_level_comment.body, re.IGNORECASE) and top_level_comment.id not in comments_replied_to:
                titles = get_titles_array_from_submission(top_level_comment.body)
                try:
                    response = ""
                    if len(titles) > 0: # if there is at least one title to respond to:
                        num_comments_replied_to += 1    # add 1 because this comment is being replied to
                        comments_replied_to.append(top_level_comment.id)
                        for title in titles:
                            response += imdb_reply_format(title)
                            response += "  \n"
                            #url = imdb_url_finder(imdb_search_parser(title))
                            #print(imdb_url_name_getter(url))
                        top_level_comment.reply(response)
                except IndexError:
                    print("still don't know why this is happening, but it still works, so I'm ok with this\n")
        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")

    print("Test replied to: ", num_posts_replied_to, " posts\n")
    print("test replied to: ", num_comments_replied_to, " comments\n")
    store_posts(posts_replied_to)
    store_comments(comments_replied_to)
    return
