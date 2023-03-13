import youtube_dl

input_url = 'https://www.youtube.com/watch?v=5Xxtq6dkG4g'
tmp_audio = "yt_tmp.mp3"

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

# YouTubeから動画をダウンロード
ydl = youtube_dl.YoutubeDL(ydl_opts)
info_dict = ydl.extract_info(input_url, download=True)