import unittest
from utils.twitter_api import get_twitter_api

class TestFollowAutomation(unittest.TestCase):

    def setUp(self):
        self.api = get_twitter_api()

    def test_follow_user(self):
        # テスト用のユーザーIDを指定
        user_id = 'test_user_id'
        result = self.api.create_friendship(user_id)
        self.assertIsNotNone(result)
        self.assertEqual(result.screen_name, 'test_user_screen_name')

if __name__ == '__main__':
    unittest.main()