"""
Main control program which handles the primary functions and twitter API handling
"""
import os
import tweepy
from .scriptreader import Tweet

SCRIPT_FILES = ["test.txt"]


def get_tokens():
    """
    function to pull the tokens once I've decided how to store them
    """
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = "ACCESS_TOKEN_SECRET"
    return consumer_key, consumer_secret, access_token, access_token_secret


def get_auth():
    """
    Authenticate to Twitter
    """
    consumer_key, consumer_secret, access_token, access_token_secret = get_tokens()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def main():
    """
    primary entrypoint
    """
    auth = get_auth
    api = tweepy.API(auth)
    tweet = Tweet(SCRIPT_FILES)
    api.update_status(tweet.generate())


if __name__ == "__main__":
    main()
