#!/bin/env python

import praw
from dotenv import load_dotenv
import os
import yaml
import argparse

load_dotenv()

reddit = praw.Reddit(
    username = os.environ["PRAW_USERNAME"],
    password = os.environ["PRAW_PASSWORD"],
    client_id = os.environ["PRAW_CLIENT_ID"],
    client_secret = os.environ["PRAW_CLIENT_SECRET"],
    user_agent = os.environ["PRAW_USER_AGENT"],
)

parser = argparse.ArgumentParser()
parser.add_argument('--subreddits', action="store_true", help="Save subcribed subreddits in subreddits.txt")
parser.add_argument('--multireddits', action="store_true", help="Save user's multireddits in multireddits.yaml")
parser.add_argument('--saved', action="store_true", help="Save saved comments and submissions in saved.yaml")
parser.add_argument('--redditor', action="store_true", help="Save redditor's submissions and comments in redditor.yaml")

args = parser.parse_args()
if args.subreddits:
    subreddits(reddit)
if args.multireddits:
    multireddits(reddit)
if args.saved:
    saved(reddit)
if args.redditor:
    redditor(reddit)

def subreddits(reddit):
    with open("subreddits.txt", "w") as file:
        for subreddit in reddit.user.subreddits(limit=None):
            file.write(str(subreddit) + "\n")

def multireddits(reddit):
    with open("multireddits.yaml", "w") as file:
        multireddits = {}
        for multireddit in reddit.user.multireddits():
            subreddits = []
            for subreddit in multireddit.subreddits:
                subreddits.append(str(subreddit))
            multireddits[multireddit.name] = subreddits
        yaml.dump(multireddits, file)

def saved(reddit):
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
                i["is_self"] = item.is_self
                i["external_link"] = False

                domains = ["redd.it","i.imgur.com","reddit.com"]
                is_media = any(domain in item.url for domain in domains)
                if not is_media and not item.is_self:
                    i["external_link"] = True

            i["id"] = item.id
            i["created_utc"] = item.created_utc
            i["permalink"] = item.permalink
            i["score"] = item.score
            saved.append(i)
        yaml.dump(saved, file)

def saved(reddit):
    with open("redditor.yaml", "w") as file:
        cs = []
        redditor = reddit.user.me()
        for comment in redditor.comments.new():
            c= {}
            c["type"] = "comment"
            c["id"] = comment.id
            c["created_utc"] = comment.created_utc
            c["permalink"] = comment.permalink
            c["score"] = comment.score
            cs.append(c)
        for submission in redditor.submissions.new():
            s= {}
            s["type"] = "submission"
            s["id"] = submission.id
            s["created_utc"] = submission.created_utc
            s["permalink"] = submission.permalink
            s["score"] = submission.score

            s["url"] = submission.url
            s["title"] = submission.title
            s["upvote_ratio"] = submission.upvote_ratio

            cs.append(s)
        yaml.dump(cs, file)

