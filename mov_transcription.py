import torch
import whisper
import pprint

input_model_size = 'small' #whisperのモデルのサイズ

source_language = 'Japanese'

tmp_audio = "interview.mp4"

def transcription(input_model_size, source_language):
    # この行を追加してPyTorchでCPUの利用を強制する
    # torch.cuda.is_available = lambda: False

    try:
        
        # 文字起こしのモデルを読み込む
        transcription_model = whisper.load_model(input_model_size)
        
        # 動画の音声データをwhisperに読み込む    
        transcription_audio = whisper.load_audio(tmp_audio)
        
        result = transcription_model.transcribe(transcription_audio, 
                                                verbose=True,
                                                language=source_language,
                                                )
        
        # pprint.pprint(result['text'])
        
        # 空白で改行して保存する
        text = result['text'].replace(' ', ' \n')
        with open("./tmp.txt", mode='w', encoding='utf-8') as f:
            f.write(text)
        
    except Exception as e:
        print(e)