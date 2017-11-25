# coding: utf-8
from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

twitter = OAuth1Session(os.environ["consumer_key"],
                        os.environ["consumer_secret"],
                        os.environ["access_token_key"],
                        os.environ["access_token_secret"]
                        )
tweets = ["文言１", "文言２", "文言３"]

randomtweet = tweets[random.randrange(len(tweets))]

timestamp = datetime.datetime.today() + datetime.timedelta(hours=9)
timestamp = str(timestamp.strftime("%Y/%m/%d%H:%M"))

params = {
    "status": randomtweet + " " + timestamp
}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)
