
import tweepy
import csv
import pandas as pd
import sys
import config


argument = sys.argv[1]
HashTag = "%23" + argument

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open(argument+'.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=HashTag,count=100,
                           lang="en",
                           since="2018-07-04").items():
    print (tweet.created_at, tweet.text, tweet.user)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.id_str])
   