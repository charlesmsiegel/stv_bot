import json
import tweepy


def send_tweet(text):
    with open("API_KEYS.json", 'r') as filename:
        auths = json.load(filename)

    auth = tweepy.OAuthHandler(auths['API_KEY'], auths['API_SECRET_KEY'])
    auth.set_access_token(auths['access_token'], auths['access_token_secret'])

    api = tweepy.API(auth)
    api.update_status(text)
