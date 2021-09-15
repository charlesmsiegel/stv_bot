import json
import tweepy


def send_tweet(text, image=None):
    with open("API_KEYS.json", 'r') as filename:
        auths = json.load(filename)

    auth = tweepy.OAuthHandler(auths['API_KEY'], auths['API_SECRET_KEY'])
    auth.set_access_token(auths['access_token'], auths['access_token_secret'])

    api = tweepy.API(auth)
    if image is not None:
        api.update_status(text, media_ids=[image])
    else:
        api.update_status(text)
