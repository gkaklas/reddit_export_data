#!/bin/env python

import praw
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

reddit = praw.Reddit(
    username = os.environ["PRAW_USERNAME"],
    password = os.environ["PRAW_PASSWORD"],
    client_id = os.environ["PRAW_CLIENT_ID"],
    client_secret = os.environ["PRAW_CLIENT_SECRET"],
    user_agent = os.environ["PRAW_USER_AGENT"],
)

with open("subreddits.txt", "w") as file:
    for subreddit in reddit.user.subreddits(limit=None):
        file.write(str(subreddit) + "\n")

with open("multireddits.yaml", "w") as file:
    multireddits = {}
    for multireddit in reddit.user.multireddits():
        subreddits = []
        for subreddit in multireddit.subreddits:
            subreddits.append(str(subreddit))
        multireddits[multireddit.name] = subreddits
    yaml.dump(multireddits, file)

with open("saved.yaml", "w") as file:
    saved = []
    redditor = reddit.user.me()
    for item in redditor.saved(limit=None):
        i= {}
        i["type"] = "comment"
        if isinstance(item, praw.models.Submission):
            i["type"] = "submission"

            i["url"] = item.url
            i["title"] = item.title
            i["upvote_ratio"] = item.upvote_ratio

        i["id"] = item.id
        i["created_utc"] = item.created_utc
        i["permalink"] = item.permalink
        i["score"] = item.score
        saved.append(i)
    yaml.dump(saved, file)

