import tweepy
import time
from config.settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from utils.openai_api import generate_reply

def automate_like_reply(api):
    with open('../data/keywords.txt') as f:
        keywords = f.read().splitlines()

    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search, q=keyword, lang='ja').items(10):
            try:
                tweet.favorite()
                print(f'Liked tweet by {tweet.user.screen_name}')
                
                # OpenAI APIを使用してリプライ内容を生成
                reply_text = generate_reply(tweet.text)
                
                api.update_status(f'@{tweet.user.screen_name} {reply_text}', in_reply_to_status_id=tweet.id)
                print(f'Replied to tweet by {tweet.user.screen_name}')
                
                time.sleep(60)  # レートリミット対応のために待機
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break