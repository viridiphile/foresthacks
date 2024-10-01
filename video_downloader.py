import yt_dlp

def download_youtube_video_and_audio(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'media/video/%(title)s.%(ext)s',  # Output template for a safe file name
        'merge_output_format': 'mp4',  # Output merged file format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'  # Convert to mp4 after merging
        }],
        'restrictfilenames': True,  # Avoid special characters in file names
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info)
        audio_file = video_file.replace('.mp4', '.m4a')  # Audio file (may need adjustment)
    
    return video_file, audio_file