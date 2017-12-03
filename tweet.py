# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
from PrepareChain import PrepareChain
from GenerateText import GenerateText
import re


consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token_key = "your_access_token_key"
access_token_secret = "your_token_secret"
twitter = OAuth1Session(consumer_key, consumer_secret, access_token_key, access_token_secret)

def search_tweet():
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    params = {"count": 200,  # ツイートを最新から何件取得するか(最大200件)
              "include_entities": True,  # エンティティ(画像のURL等)をツイートに含めるか
              "exclude_replies": True,  # リプライを含めるか
              }

    req = twitter.get(url, params=params)
    timeline = json.loads(req.text)
    words = """"""
    for tweet in timeline:
        words += tweet["text"]
    words = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", words)
    words = re.sub('RT', "", words)
    words = re.sub('お気に入り', "", words)
    words = re.sub('まとめ', "", words)
    # words = re.sub(r'[!-~]', "", words)  # 半角記号,数字,英字
    words = re.sub(r'[︰-＠]', "", words)  # 全角記号
    # words = re.sub('\n', " ", words)  # 改行文字
    return words

text = search_tweet()
chain = PrepareChain(text)
triplet_freqs = chain.make_triplet_freqs()
chain.save(triplet_freqs, True)

generator = GenerateText()
tweets = generator.generate()
params = {
    "status": tweets
}
url = "https://api.twitter.com/1.1/statuses/update.json"
req = twitter.post(url, params=params)
