import logging
from utils.twitter_api import get_twitter_api
from scripts.follow_automation import automate_following
from scripts.like_reply_automation import automate_like_reply

# ロギング設定の読み込み
from config.logging_config import logger

def main():
    logger.info("Starting Twitter Follower Boost application")

    # Twitter APIの初期化
    api = get_twitter_api()

    # フォロー自動化の実行
    logger.info("Running follow automation")
    automate_following(api)

    # いいね・リプライ自動化の実行
    logger.info("Running like and reply automation")
    automate_like_reply(api)

    logger.info("Twitter Follower Boost application finished")

if __name__ == '__main__':
    main()