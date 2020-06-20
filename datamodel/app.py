import tweepy
import os 
import keyring
import pandas as pd
import numpy as np
import string 

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask (__name__, static_folder='app', static_url_path="/app")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://127.0.0.1:5432/tt'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Tweets 
from models import Hashtags
from models import Atuser 