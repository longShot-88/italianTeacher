#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Generate a List of the most common word in the Home timeLine '''

import twitter
import json
from collections import Counter # Find frequency
from prettytable import PrettyTable # print a nice table of results
import webbrowser

old = ['rt', 'in', 'the', 'to', 'a', 'of', 'ty!', 'is', 'de', 'and', 'for',
'with', 'on', 'you', 'via', 'en', 'that', 'your', '-', 'by', 'mayweather',
'pacquiao', 'at', 'la', 'be', 'floyd', 'it', '']

CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN,  OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

home_tweets = twitter_api.statuses.home_timeline(count=200)
tweets = [status['text'] for status in home_tweets]
words = [word for tweet in tweets 
			  for word in tweet.split()
			  if (word.lower() not in old) and ('@' not in word)
			  and ('#' not in word)]

table = PrettyTable(field_names=['Word', 'Count'])

c = Counter(words)
common = c.most_common()

print common
