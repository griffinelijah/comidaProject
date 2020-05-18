import tweepy
import os
import csv

consumer_key="l1zfKK3iqXdXGtm1AaXp21Vg3"
consumer_secret="w5PL9dxaIPlqmQz2DqcLWbawUEFPhI8IOPA8y2JuQIF9dWWuQp"

access_token="3633899837-feHjeMHL6aqzYV3RQKfuEqr7g6jXzslSj4GyjzD"
access_secret="o1Nj5xAoF8p1T0leQDBXSjKcxYkr1CLcgpY91QfHdfgF1"

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
mass_search = api.search("#COVID19 -filter:retweets", lang="en", tweet_mode='extended', count=500)

#this will write the results of the search into a csv file called script_results.csv
with open('script_results.csv', 'w', newline='', encoding='utf-8') as f:
  for tweet in mass_search:
      csv_writer = csv.writer(f)
      #this writes a new row for each returned result removing commas
      csv_writer.writerow(tweet.full_text.split(','))
      # print(tweet.full_text)



