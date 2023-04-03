import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.environ.get("OPENAI_API_KEY")

def summerize():
  # UTF8エンコードのテキストファイルの読み込み
  with open('./tmp.txt', encoding='utf-8') as f:
      text = f.read()

  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {"role": "user", "content": "以下の文章を要約してください。"},
      {"role": "user", "content": text}
    ]
  )

  with open("./sum.txt", mode='w', encoding='utf-8') as f:
      f.write(completion.choices[0].message.content)
      
  return completion.choices[0].message.content

if __name__ == "__main__":
  print(summerize())