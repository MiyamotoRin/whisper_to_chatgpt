import os
import sys
import whisper
import openai
from dotenv import load_dotenv

load_dotenv(".env")

input_model_size = 'small' #whisperのモデルのサイズ

source_language = 'Japanese'

def transcription(audio_file, source_language):
    # この行を追加してPyTorchでCPUの利用を強制する
    # torch.cuda.is_available = lambda: False

    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        audio = open(audio_file, 'rb')
        result = openai.Audio.translate("whisper-1", audio)
        
        with open("./tmp.txt", mode='w', encoding='utf-8') as f:
            f.write(result['text'])
        
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
  if len(sys.argv) > 1:
      input_file = sys.argv[1]
      print(transcription(input_file, source_language))
  else:
      print("Usage: python mov_transcription.py <path_to_text_file>")