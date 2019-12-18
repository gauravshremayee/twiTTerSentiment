import tweepy
import sys
import csv
import pandas as pd
####input your credentials here
#login to https://developer.twitter.com/en/apps to get the below keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file to append data
csvFile = open('file.csv', 'a')
csvWriter = csv.writer(csvFile)


hashTag=sys.argv[1]
for tweet in tweepy.Cursor(api.search,q=hashTag,count=100000,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
