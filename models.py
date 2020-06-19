from app import db
from sqlalchemy import Table, MetaData, Text, Column
from sqlalchemy.sql import text
from sqlalchemy.engine import create_engine


# Create all the Tables

class Tweets(db.Model):
    __tablename__ = 'tweets2'

    id = db.Column(db.String(), primary_key=True,autoincrement=False)
    text = db.Column(db.String())
    dttm = db.Column(db.DateTime(timezone=True))
    isRetweet = db.Column(db.Boolean())

    def __init__(self, tweet_id, text, dttm, isRetweet):
        self.tweet_id = tweet_id
        self.text = text
        self.dttm = dttm
        self.isRetweet = isRetweet

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Hashtags(db.Model):
    __tablename__ = 'hashtags'

    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets2.id'))
    tag = db.Column(db.String())

    def __init__(self, tweet_id, tag):
        self.tweet_id = tweet_id
        self.tag = tag

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Atuser(db.Model):
    __tablename__ = 'atuser'

    id = db.Column(db.Integer, primary_key=True)
    tweet_id = db.Column(db.Integer, db.ForeignKey('tweets2.id'))
    screen_name = db.Column(db.String())

    def __init__(self, tweet_id, screen_name):
        self.tweet_id = tweet_id
        self.screen_name = screen_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
