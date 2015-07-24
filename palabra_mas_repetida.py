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

google_tans = 'https://translate.google.com/#en/it/' +common[:1][0][0]
webbrowser.open(google_tans, new=0)
 
for word_freq in common[:8]:
 	# add a tuple(word_freq, freq)
 	table.add_row(word_freq)
# Adjust aligment to left for word colum and right for count
table.align['Word'] = 'l'
table.align['Count'] = 'r'

for t in tweets[:2]:
	print t.encode('utf-8')
print 	
print table	
