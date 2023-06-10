#!/bin/env python

import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    username = os.environ["PRAW_USERNAME"],
    password = os.environ["PRAW_PASSWORD"],
    client_id = os.environ["PRAW_CLIENT_ID"],
    client_secret = os.environ["PRAW_CLIENT_SECRET"],
    user_agent = os.environ["PRAW_USER_AGENT"],
)

