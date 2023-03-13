import torch
import os
import subprocess
import whisper
import youtube_dl
import pprint

input_model_size = 'small' #whisperのモデルのサイズ

input_url = 'https://www.youtube.com/watch?v=5Xxtq6dkG4g'
output_file = 'result_' + input_model_size + '.txt'
source_language = 'Japanese'

# YouTubeからmp3形式でダウンロードするよう指定する
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "yt_tmp" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

tmp_audio = "interview.mp4"

# この行を追加してPyTorchでCPUの利用を強制する
# torch.cuda.is_available = lambda: False

try:
    
    # 文字起こしのモデルを読み込む
    transcription_model = whisper.load_model(input_model_size)
    
    # 動画の音声データをwhisperに読み込む    
    transcription_audio = whisper.load_audio(tmp_audio)
    # trim_audio = whisper.pad_or_trim(transcription_audio)
    
    # make log-Mel spectrogram and move to the same device as the model
    # わからなかったのでコピペ、多分CPUかGPUかの選択
    # mel = whisper.log_mel_spectrogram(transcription_audio).to("cuda")
    
    # options = whisper.DecodingOptions(language=source_language,
    #                                   without_timestamps=True,
    #                                   fp16=False
    #                                   )
    
    # result = whisper.decode(transcription_model, mel, options)
    
    result = transcription_model.transcribe(transcription_audio, 
                                            verbose=True,
                                            language=source_language,
                                            )
    
    # pprint.pprint(result['text'])
    
    # 句点で改行して保存する
    text = result['text'].replace(' ', ' \n')
    with open("./tmp.txt", mode='w', encoding='utf-8') as f:
        f.write(text)
    
except Exception as e:
    print(e)