import tweepy
from textblob import TextBlob
import pandas as pd
import os

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

def check_sentiment(number):
	if number > 0:
		number = 'positive'
	elif number < 0:
		number = 'negative'
	else:
		number = 'neutral'
	return number

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("trump")

data_dict = {'tweet': [], 'sentiment': []}

for tweet in public_tweets:
	# print(tweet.text)
	# print(" ")
	# print(" ")
	analysis = TextBlob(tweet.text)
	# print(" ")
	# print(analysis.sentiment.polarity)
	# print(" ")
	sentiment = check_sentiment(analysis.sentiment.polarity)
	# print(sentiment)
	data_dict['tweet'].append(tweet.text) 
	data_dict['sentiment'].append(sentiment)

# # print(data_dict)
# print(pd.DataFrame(data_dict))


data_dict = pd.DataFrame(data_dict)
# print(data_dict)
data_dict = data_dict[['tweet', 'sentiment']]
# print(os.getcwd())
data_dict.to_csv("sentiment_tweets.csv", index = False)











