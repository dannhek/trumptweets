import tweepy
import os 
import keyring
import pandas as pd
import numpy as np
import string 
import time
from sqlalchemy import create_engine

# Pull in Passwords
exec(open('./consumerpy').read())

# Open the Connection to Twitter
auth = tweepy.OAuthHandler(keyring.get_password('trumptweets','TWITTER_KEY'),keyring.get_password('trumptweets','TWITTER_SECRET'))
auth.set_access_token(keyring.get_password('trumptweets','TWITTER_TOKEN'), keyring.get_password('trumptweets','TWITTER_TOKEN_SEC'))
api = tweepy.API(auth,wait_on_rate_limit=True,retry_count=20,retry_delay=10,retry_errors=[401, 404, 500, 503],wait_on_rate_limit_notify=True)

# Target Acquired
username = 'WhiteHouse'
user = api.get_user(username)

# Function to populate data model
def import_tweets_to_db(tweets, db_str = 'postgres://127.0.0.1:5432/tt'):
    eng = create_engine(db_str)
    df = pd.DataFrame({
        'id'        : [str(tweet.id) for tweet in tweets],
        'text'      : [tweet.text for tweet in tweets],
        'dttm'      : [tweet.created_at for tweet in tweets],
        'isRetweet' : [tweet.text[0:2] == 'RT' for tweet in tweets]
    })
    df.to_sql('tweets', con = eng, if_exists='append', index=False)
    print(df.shape)
    for tweet in tweets:
        tokens = [s.rstrip(string.punctuation) for s in tweet.text.replace('\n',' ').split(' ')]
        hashtags = list(filter(lambda k: k.startswith('#'), tokens))
        userrefs = list(filter(lambda k: k.startswith('@'), tokens))
        if (len(hashtags) > 0) :
            h = {
            'tweet_id' : np.repeat(str(tweet.id),len(hashtags)),
            'line'     : list(range(max(len(hashtags),0))),
            'hashtag'  : hashtags
            }
            pd.DataFrame(h).to_sql('hashtags',con = eng,if_exists='append',index=False)
        if (len(userrefs) > 0) :
            u = {
            'tweet_id' : np.repeat(str(tweet.id),len(userrefs)),
            'line'     : list(range(max(len(userrefs),0))),
            'users'    : userrefs
            }
            pd.DataFrame(u).to_sql('atusers',con = eng,if_exists='append',index=False)


# Get the tweets, 199 at a time
last_id = None
for i in range(100):
    tweets = api.user_timeline(screen_name = user.screen_name, count=199, max_id = last_id, since_id = 1)
    ids = [tweet.id for tweet in tweets]
    if (len(ids)==0):
        #Made it through Everything... or something bombed
        print('Empty')
        break
    if (min(ids)==last_id):
        #Pulled the same thing again
        print('Same Last ID')
        break
    last_id = min(ids)-1
    print(last_id)
    import_tweets_to_db(tweets=tweets)





tweets = api.user_timeline(screen_name = 'EconTalker', count = 300)
df = pd.DataFrame({
    'id'        : [str(tweet.id) for tweet in tweets],
    'text'      : [tweet.text for tweet in tweets],
    'dttm'      : [tweet.created_at for tweet in tweets],
    'isRetweet' : [tweet.text[0:2] == 'RT' for tweet in tweets]
    'tweeter'   : [tweet.user.screen_name for tweet in tweets]
})
df.shape
