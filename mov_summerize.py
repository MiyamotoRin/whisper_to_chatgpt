import torch
import os
import subprocess
import whisper
import youtube_dl

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

tmp_audio = "yt_tmp.mp3"
# if(os.path.exists(tmp_audio)):
#     os.remove(tmp_audio)

# この行を追加してPyTorchでCPUの利用を強制する
# torch.cuda.is_available = lambda: False

try:
    # YouTubeから動画をダウンロード
    # ydl = youtube_dl.YoutubeDL(ydl_opts)
    # info_dict = ydl.extract_info(input_url, download=True)
    
    # 文字起こしのモデルを読み込む
    transcription_model = whisper.load_model(input_model_size)
    
    # 動画の音声データをwhisperに読み込む    
    transcription_audio = whisper.load_audio(tmp_audio)
    
    # make log-Mel spectrogram and move to the same device as the model
    # わからなかったのでコピペ、多分CPUかGPUかの選択
    mel = whisper.log_mel_spectrogram(transcription_audio).to("cuda")
    
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(transcription_model, mel, options)
    
except Exception as e:
    print(e)