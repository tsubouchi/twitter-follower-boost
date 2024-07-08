twitter-follower-boost/
│
├── config/
│   ├── settings.py          # APIキーなどの設定情報
│   ├── logging_config.py    # ログ設定
│
├── scripts/
│   ├── follow_automation.py # フォロー自動化スクリプト
│   ├── like_reply_automation.py # いいね・リプライ自動化スクリプト
│
├── data/
│   ├── target_accounts.txt  # ターゲットアカウントリスト
│   ├── keywords.txt         # キーワードリスト
│
├── logs/
│   ├── app.log              # ログファイル
│
├── tests/
│   ├── test_follow_automation.py # フォロー自動化のテスト
│   ├── test_like_reply_automation.py # いいね・リプライ自動化のテスト
│
├── utils/
│   ├── twitter_api.py       # Twitter APIのユーティリティ
│   ├── data_processing.py   # データ処理のユーティリティ
│
├── main.py                  # メインスクリプト
├── requirements.txt         # 依存パッケージ
├── README.md                # プロジェクトの概要
├── .env                     # 環境変数（APIキーなど）
└── .gitignore               # Gitで無視するファイルリスト