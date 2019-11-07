"""
secret: OzcivV6aBZriJb7lFsU54QQJuUU
id:		wJhXch1ro-Dn0A
"""

import praw

# Create our Reddit client (lets us communicate with Reddit)
reddit = praw.Reddit(client_id='wJhXch1ro-Dn0A',
                     client_secret='OzcivV6aBZriJb7lFsU54QQJuUU',
                     user_agent='rufhvbp')

# Go through the first 10 hot posts in the uwaterloo subreddit
for submission in reddit.subreddit('uwaterloo').hot(limit=10):
    print(submission.title)

canada_universities = [
    "UofT",
    "uwaterloo",
    "uAlberta",
    "UBC",
    # And everyone's favourite
    "nipissingu"
]

for university in canada_universities:
    print("Top Posts in University: %s" % university)
    for submission in reddit.subreddit(university).hot(limit=10):
        print("\t %s" % submission.title)