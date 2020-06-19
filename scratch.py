import tweepy
import os 
import keyring
import pandas as pd
import numpy as np
import string 
import psycopg2

from models import Tweets 
from sqlalchemy import create_engine

# Pull in Passwords
exec(open('./consumerpy').read())

# Open the Connection to Twitter
auth = tweepy.OAuthHandler(keyring.get_password('trumptweets','TWITTER_KEY'),keyring.get_password('trumptweets','TWITTER_SECRET'))
auth.set_access_token(keyring.get_password('trumptweets','TWITTER_TOKEN'), keyring.get_password('trumptweets','TWITTER_TOKEN_SEC'))
api = tweepy.API(auth)

# Open Connection to Database
connection = psycopg2.connect(
    database = 'tt',
    user = 'dhek',
    host = 'localhost'
)
cursor = connection.cursor()

# Trying shit
username = 'realDonaldTrump'
user = api.get_user(username)
print(user.followers_count)

tweets = api.user_timeline(screen_name = user.screen_name, count = 200)


df = pd.DataFrame(data=[str(tweet.id) for tweet in tweets], columns=['id'])
df['text'] = [tweet.text for tweet in tweets]
df['dttm'] = [tweet.created_at for tweet in tweets]
df['isRetweet'] = [tweet.text[0:2] == 'RT' for tweet in tweets]

eng = create_engine('postgres://127.0.0.1:5432/tt')
df.to_sql('tweets',con = eng,if_exists='append',index=False)

for tweet in tweets:
    # ignore retweets for now
    # if (tweet.text[0:2] == 'RT'): 
    #     continue 
    print([tweet.created_at, tweet.source, tweet.id])
    tokens = [s.rstrip(string.punctuation) for s in tweet.text.replace('\n',' ').split(' ')]
    hashtags = list(filter(lambda k: k.startswith('#'), tokens))
    userrefs = list(filter(lambda k: k.startswith('@'), tokens))
    if len(hashtags) > 0 :
        h = {
            'tweet_id' : np.repeat(str(tweet.id),len(hashtags)),
            'line'     : list(range(max(len(hashtags),0))),
            'hashtag'  : hashtags
        }
        pd.DataFrame(h).to_sql('hashtags',con = eng,if_exists='append',index=False)
    if len(userrefs) > 0 :
        u = {
            'tweet_id' : np.repeat(str(tweet.id),len(userrefs)),
            'line'     : list(range(max(len(userrefs),0))),
            'users'    : userrefs
        }
        pd.DataFrame(u).to_sql('atusers',con = eng,if_exists='append',index=False)

