import torch
import os
import subprocess

import youtube_dl

# tkinterのインポート
import tkinter as tk

model_size = 'small' #whisperのモデルのサイズ

# input_url = 'https://www.youtube.com/watch?v=DerrX7XoLDc'
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

def yt_to_txt(model_size, input_url, source_language):
    try:
        # YouTubeから動画をダウンロード
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(input_url, download=True)

        # モデルを指定して文字起こし
        subprocess.run('whisper ' + tmp_audio 
                       + ' --language ' + str(source_language) 
                       + ' --model ' + str(model_size) 
                       + ' --output_format txt'
                       + ' --device cpu'
                       + ' --output_dir ./', shell=True)
        
    except Exception as e:
        print(e)


# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("350x100")

# テキストボックス設置 <---追加するコード
url_box = tk.Entry(width = 40)
url_box.place(x = 10, y = 10)

# Runボタン設置
run_button = tk.Button(root, text = "Run", 
                       command = yt_to_txt(model_size, url_box.get(), source_language))
run_button.place(x = 160, y = 40)

# ウインドウ状態の維持
root.mainloop()
