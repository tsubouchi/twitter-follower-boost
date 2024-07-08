import unittest
from utils.twitter_api import get_twitter_api

class TestLikeReplyAutomation(unittest.TestCase):

    def setUp(self):
        self.api = get_twitter_api()

    def test_like_tweet(self):
        # テスト用のツイートIDを指定
        tweet_id = 'test_tweet_id'
        result = self.api.create_favorite(tweet_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.id_str, tweet_id)

    def test_reply_tweet(self):
        # テスト用のツイートIDを指定
        tweet_id = 'test_tweet_id'
        reply_text = 'テストリプライ'
        result = self.api.update_status(status=reply_text, in_reply_to_status_id=tweet_id)
        self.assertIsNotNone(result)
        self.assertIn(reply_text, result.text)

if __name__ == '__main__':
    unittest.main()