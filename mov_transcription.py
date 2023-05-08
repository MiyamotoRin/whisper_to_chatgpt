import sys
import torch
import whisper
import pprint

input_model_size = 'small' #whisperのモデルのサイズ

source_language = 'Japanese'

def transcription(audio_file, source_language):
    # この行を追加してPyTorchでCPUの利用を強制する
    # torch.cuda.is_available = lambda: False

    try:
        
        # 文字起こしのモデルを読み込む
        transcription_model = whisper.load_model(input_model_size)
        
        # 動画の音声データをwhisperに読み込む    
        transcription_audio = whisper.load_audio(audio_file)
        
        # 言語を指定して文字起こしを実行する
        options = dict(language="English", beam_size=5, best_of=5)
        translate_options = dict(task="translate", **options)
        
        # result = transcription_model.transcribe(transcription_audio, 
        #                                         verbose=True,
        #                                         language=source_language,
        #                                         )
        
        result = transcription_model.transcribe(transcription_audio,
                                                verbose=True,
                                                **translate_options)
        
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