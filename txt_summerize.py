import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.environ.get("OPENAI_API_KEY")

# UTF8エンコードのテキストファイルの読み込み
with open('./tmp.txt', encoding='utf-8') as f:
    text = f.read()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Please summerize this text."},
    {"role": "user", "content": text}
  ]
)

print(completion.choices[0].message.content)