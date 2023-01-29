import torch
import os
import subprocess

import youtube_dl

model_size = 'small' #whisperのモデルのサイズ

input_url = 'https://www.youtube.com/watch?v=DerrX7XoLDc'
output_file = 'result_' + model_size + '.txt'
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

tmp_audio = 'yt_tmp.mp3'
if(os.path.exists(tmp_audio)):
    os.remove(tmp_audio)

# この行を追加してPyTorchでCPUの利用を強制する
# torch.cuda.is_available = lambda: False

try:
    # YouTubeから動画をダウンロード
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(input_url, download=True)

    # モデルを指定して文字起こし
    subprocess.run('whisper ' + tmp_audio + ' --language ' + str(source_language) + ' --model ' + str(model_size) + ' --output_format txt', shell=True)
    
except Exception as e:
    print(e)