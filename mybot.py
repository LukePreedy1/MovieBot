import praw

reddit = praw.Reddit(client_id='EQPyHaA6U5GIdA',
                     client_secret='jAI6cKXM-MKT1Une4S9x4xB4E0g',
                     user_agent='MovieBot',
                     username='MovieBot0451',
                     password='Destructive01')

print(reddit.read_only)

#TODO change this when the bot is complete
subreddit = reddit.subreddit('movies')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.hot(limit=10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post
