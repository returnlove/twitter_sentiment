import tweepy
from textblob import TextBlob

consumer_key = "iguIihI2T2LstZtTaihLKjnrY"
consumer_secret = "RAyfOKivniDu2XlGMx2adCsiDTg17kldvbOcJOA6iThG3BGHTY"

access_token = "742220055002243072-hyS8kunykG2eBaQA7qhJfDn0WzY7Dg9"
access_token_secret = "kKHhFVzzw4NvhmMKFInLOwHrlQkVctA5xzcqYLtYXf2gB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("trump")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print(" ")

