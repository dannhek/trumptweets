import tweepy
import os 
import keyring
import pandas as pd
import numpy as np
import string 

from models import Tweets 

# Pull in Passwords
exec(open('./consumerpy').read())

# Open the Connection to Twitter
auth = tweepy.OAuthHandler(keyring.get_password('trumptweets','TWITTER_KEY'),keyring.get_password('trumptweets','TWITTER_SECRET'))
auth.set_access_token(keyring.get_password('trumptweets','TWITTER_TOKEN'), keyring.get_password('trumptweets','TWITTER_TOKEN_SEC'))
api = tweepy.API(auth)

# Trying shit
username = 'realDonaldTrump'
user = api.get_user(username)
print(user.followers_count)

tweets = api.user_timeline(screen_name = user.screen_name)


df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
df['id'] = np.array([tweet.id for tweet in tweets])
df['len'] = np.array([len(tweet.text) for tweet in tweets])
df['date'] = np.array([tweet.created_at for tweet in tweets])
df['source'] = np.array([tweet.source for tweet in tweets])
df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
df['is_retweet'] = np.array([tweet.text[0:2] == 'RT' for tweet in tweets])

for tweet in tweets:
    # ignore retweets for now
    # if (tweet.text[0:2] == 'RT'): 
    #     continue 
    print([tweet.created_at, tweet.source, tweet.id])
    tokens = [s.rstrip(string.punctuation) for s in tweet.text.replace('\n',' ').split(' ')]
    hashtags = list(filter(lambda k: k.startswith('#'), tokens))
    userrefs = list(filter(lambda k: k.startswith('@'), tokens))
    print(hashtags)
    print(userrefs)
