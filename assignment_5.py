# -*- coding: utf-8 -*-
"""assignment 5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G9q89n-Rbmub7WHLZk7iZZcrW-llGAOx

# Import packages
"""

import nltk
import re
import spacy
import time
import tweepy
import webbrowser

import nltk.corpus

nl = spacy.load('en_core_web_sm')
nltk.download('stopwords')

from nltk.corpus import stopwords

"""# Authentication"""

# insert api_key and api_secret_key below
api_key = 'insert api key here'
api_secret_key = 'insert api secret key here'

auth = tweepy.OAuthHandler(api_key, api_secret_key)

# insert user pin below
pin = "insert user pin here"

auth.get_access_token(pin)

api = tweepy.API(auth)

user = api.get_user('twitter')

"""# Create StreamListener"""

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=1):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        tweet.append(status.text)

        if (time.time() - self.start_time) < self.limit:
            return True
        else:
            return False

"""# Preprocess tweets"""

def preprocess(observations):

    for element in range(len(observations)): 
        letters_only_text = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", '', observations[element], flags=re.MULTILINE)
        letters_only_text = re.sub(r'[^a-zA-Z\s]', " ", letters_only_text)

        words = letters_only_text.lower().split()
        
        additional  = ['rt','rts','retweet']
        stopword_set = set().union(stopwords.words('english'), additional)
        significant = [w for w in words if w not in stopword_set]
        
        observations[element] = " ".join(significant)

    return observations

"""# Identify labels"""

def addLabel(observations, dictionary_label_word_count):
  for element in range(len(observations)): 
      tweet_element = nl(observations[element])

      for entity in tweet_element.ents:
        if entity.label_ not in dictionary_label_word_count.keys(): 
          dictionary_label_word_count[entity.label_] = {}
          dictionary_label_word_count[entity.label_][entity.text] = 1
        else:                                          
          if entity.text not in dictionary_label_word_count[entity.label_].keys():
            dictionary_label_word_count[entity.label_][entity.text] = 1
          else:
            dictionary_label_word_count[entity.label_][entity.text] += 1

"""# Print Named Entities"""

def printEntities(dictionary_label_word_count):
  labels = 0
  entities = 0

  for label in dictionary_label_word_count:
    labels += 1
    for entity in dictionary_label_word_count[label]:
      entities += 1
      print(entity, "-", dictionary_label_word_count[label][entity])

  print('\n', 'Distinct Named Entities: ', entities)

"""# StreamListener for 30 seconds"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=30))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)

"""# StreamListener for 1 minute"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=60))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)

"""# StreamListener for 2 minutes"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=120))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)

"""# StreamListener for 3 minutes"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=180))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)

"""# StreamListener for 4 minutes"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=240))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)

"""# StreamListener for 5 minutes"""

tweet = []
dictionary_label_word_count = {}

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=300))
myStream.filter(track=['Joe Biden'])

preprocess(tweet)
addLabel(tweet, dictionary_label_word_count)
printEntities(dictionary_label_word_count)