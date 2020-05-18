import tweepy
import os
import csv

consumer_key=
consumer_secret=

access_token=
access_secret=

#lines 4-8 are keys specific to the twitter developer account that are obtained from the twitter for dev portal. for security reasons they were not uploaded to github but can be manually filled in to run the scripts

auth = tweepy.OAuthHandler(consumer_key, 
consumer_secret)
#consumer key and secret wil be obtained from twitter developer account
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth)

# #this will return data for all saved searches. currently only saved search term is #covid19
# saved_search = api.get_saved_search(1257727687801614336)
# #iterate over all the return search data and print only text of each to the console
# print(saved_search)

#this will do a mass query over twitter search for a given keyword.
#the first parameter that is passed in is the keyword to be searched 
#all retweets are filtered out as the api can sometimes return incomplete retweets 
#the count parameter can be passed through to restrict the amount of search results returned
#the lang parameter uses ISO 639-1 two letter codes to restrict language, en is for english
#tweet mode is set to extended to gather full tweet regardless of character length
covid19_search = api.search("#COVID19 -filter:retweets -filter:links", lang="en", tweet_mode='extended', count=500)
covid_search = api.search("#COVID -filter:retweets -filter:links", lang="en", tweet_mode='extended', count=500)
coronavirus_search = api.search("#coronavirus -filter:retweets -filter:links", lang="en", tweet_mode='extended', count=500)

#this will write the results of the search into a separate csv file called according to the search term, more can be added by following the same format for better organization until it's added into a database
with open('covid19_results.csv', 'w', newline='', encoding='utf-8') as f:
  for tweet in covid19_search:
      csv_writer = csv.writer(f)
      #this writes a new row for each returned result removing commas
      csv_writer.writerow(tweet.full_text.split(','))
      # print(tweet.full_text)

with open('covid_results.csv', 'w', newline='', encoding='utf-8') as f:
  for tweet in covid19_search:
      csv_writer = csv.writer(f)
      #this writes a new row for each returned result removing commas
      csv_writer.writerow(tweet.full_text.split(','))
      # print(tweet.full_text)

with open('coronavirus_results.csv', 'w', newline='', encoding='utf-8') as f:
  for tweet in covid19_search:
      csv_writer = csv.writer(f)
      #this writes a new row for each returned result removing commas
      csv_writer.writerow(tweet.full_text.split(','))
      # print(tweet.full_text)



