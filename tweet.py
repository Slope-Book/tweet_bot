import os
from datetime import datetime

import twitter

api = twitter.Api(consumer_key=os.environ["consumer_key"],
                  consumer_secret=os.environ["consumer_secret"],
                  consumer_token_key=os.environ["access_token_key"],
                  consumer_token_secret=os.environ["access_token_secret"]
                  )
api.PostUpdate("system time is %s" % datetime.now())
