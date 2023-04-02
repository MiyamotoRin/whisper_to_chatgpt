import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'm4a/bestaudio',  # Download the best quality video
        'outtmpl': 'tmp.%(ext)s',  # Save the downloaded video with its title as the filename
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)