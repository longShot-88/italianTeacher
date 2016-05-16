#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Generate a List of the most common words in the Home timeLine '''

import twitter
from collections import Counter # Find frequency

def login():
    CONSUMER_KEY = ''
    CONSUMER_SECRET =''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    auth = twitter.oauth.OAuth(OAUTH_TOKEN,  OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)

def common_home_words():
    twitter_api = login()
    home_tweets = twitter_api.statuses.home_timeline(count=200)
    tweets = [status['text'] for status in home_tweets]
    words = [word for tweet in tweets
			  for word in tweet.split()
			  if  ('@' not in word)
			  and ('#' not in word)]
    c = Counter(words)
    return c.most_common()
