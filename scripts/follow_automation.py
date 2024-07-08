import tweepy
import time
from config.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def automate_following(api):
    with open('../data/target_accounts.txt') as f:
        target_accounts = f.read().splitlines()

    for account in target_accounts:
        for follower in tweepy.Cursor(api.followers, screen_name=account).items():
            try:
                follower.follow()
                print(f'Followed {follower.screen_name}')
                time.sleep(60)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break