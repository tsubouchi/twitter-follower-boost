import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_reply(tweet_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"以下のツイートに対して適切な返信を日本語で生成してください:\n\n{tweet_text}\n\n返信:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()