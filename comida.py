import tweepy
import os

consumer_key="l1zfKK3iqXdXGtm1AaXp21Vg3"
consumer_secret="w5PL9dxaIPlqmQz2DqcLWbawUEFPhI8IOPA8y2JuQIF9dWWuQp"

access_token="3633899837-feHjeMHL6aqzYV3RQKfuEqr7g6jXzslSj4GyjzD"
access_secret="o1Nj5xAoF8p1T0leQDBXSjKcxYkr1CLcgpY91QfHdfgF1"

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
#the first parameter passed in the keyword to be searched then the array is iterated over to print out just the text of the tweet
mass_search = api.search("#COVID19", count=5, lang="en")
#the count parameter can be passed through to restrict the amount of search results returned
#the lang parameter uses ISO 639-1 two letter codes to restrict language, en is for english
for tweet in mass_search:
  print(tweet.text)



# api = tweepy.API(auth)
# for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#     print(tweet.text)
