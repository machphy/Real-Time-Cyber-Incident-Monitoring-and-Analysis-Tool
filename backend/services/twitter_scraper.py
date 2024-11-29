import tweepy

def fetch_twitter_data():

    auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET')   #twit api use krna hai ayaha
    api = tweepy.API(auth)
    tweets = api.search(q='cyber incident', count=100)
    return tweets

