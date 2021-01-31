#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: anku255 (https://gist.github.com/anku255/0cebd75cce675f2b56de1ef48ec06575)
import sys
import csv
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

#method to get a user's last 100 tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	number_of_tweets = 200

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[tweet.text.encode("utf-8")] for tweet in tweets]

	#write to a new csv file from the array of tweets
	print ("writing to {0}_tweets.csv".format(username))
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':
        #get input for username
        Username = input("Enter the Twitter Username: ")
        get_tweets(Username)
    