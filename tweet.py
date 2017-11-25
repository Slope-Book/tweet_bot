import os
from datetime import datetime

import twitter

auth = twitter.Oath(consumer_key=os.environ["consumer_key"],
                  consumer_secret=os.environ["consumer_secret"],
                  consumer_token_key=os.environ["access_token_key"],
                  consumer_token_secret=os.environ["access_token_secret"]
                  )
t = twitter.Twitter(auth=auth)
t.statuses.update(statuses="pythonからtwitterへの投稿テストです！")
