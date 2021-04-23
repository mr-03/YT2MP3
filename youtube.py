import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':'tmp' + '/%(title)s.%(ext)s',
}

def get_filename(yt_url):
    video_title = ""
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(yt_url, download=False)
        video_title = ydl.prepare_filename(info_dict)
    return video_title

def download_mp3(yt_url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])