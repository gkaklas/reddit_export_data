# About
Since in a few days I probably won't be able to freely or easily download my data from Reddit, I wrote this simple client to download them and save them in YAML.

You can also make a data request [here](https://www.reddit.com/settings/data-request), but I'm not sure about the provided data format, and they say it may take up to 30 days to generate the archive (??). (It's been a couple of days since I made the request and there is no feedback; for comparison, [Facebook](https://www.facebook.com/dyi/) responds with a link to an archive with all messages, media and metadata in JSON after a few minutes)

# Usage

## Create a Reddit app

First you need to create an app at https://old.reddit.com/prefs/apps/, then enter your client id, client secret, username and password in the `.env` file. (I don't like using the username and password, but unfortunately I couldn't make [OAuth](https://praw.readthedocs.io/en/v7.7.0/getting_started/authentication.html#code-flow) work)

You can read about setting the recommended user agent [here](https://praw.readthedocs.io/en/v7.7.0/getting_started/quick_start.html#prerequisites) and [here](https://github.com/reddit-archive/reddit/wiki/API#rules). TL;DR: `<platform>:<app ID>:<version string> (by u/<Reddit username>)`.

## Running

If you have [just](https://github.com/casey/just), you can `just run -h` to run this utility. Otherwise, prepare an environment with:

```shell
python -m venv ./venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
```

Then run with `python ./main.py -h` to see available options.

## Options

* `--subreddits`: Writes a list of your subscribed subreddits in `subreddits.txt`, one subreddit name per line.
* `--multireddits`: Saves your multireddits and their subreddits in `multireddits.yaml`
* `--redditor`: Saves your posts and comments with some metadata in `redditor.yaml`
* `--saved`: Saves your saved posts and comments with some metadata in `saved.yaml`. I have also added some [super advanced logic](https://codeberg.org/gkaklas/reddit_export_data/src/commit/b564d130ff8f501f5dd034eb0acc92a8f716b98d/main.py#L40-L43) to tag posts linking to external domains, for e.g. blog posts, articles etc
