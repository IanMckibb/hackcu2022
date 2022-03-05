import os
import tweepy

API_KEY = os.environ.get("TWITTER_API")
SECRET_KEY = os.environ.get("TWITTER_SECRET")
BEARER_KEY = os.environ.get("TWITTER_BEARER")
ACCESS_KEY = os.environ.get("TWITTER_ACCESS")
ACCESS_SECRET_KEY = os.environ.get("TWITTER_ACCESS_SECRET")
print(API_KEY)
print(SECRET_KEY)
print(ACCESS_KEY)
print(ACCESS_SECRET_KEY)
print(BEARER_KEY)
auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET_KEY)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)