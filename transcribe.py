import os
from dotenv import load_dotenv
from video_downloader import download_youtube_video_and_audio
import database

load_dotenv()

# Setup the database
database.setup_db()

def process_videos(video_urls):
    for url in video_urls:
        print(f"Processing {url}...")
        
        # Download video and audio
        video_file, audio_file = download_youtube_video_and_audio(url)

        if video_file and audio_file:
            print(f"Downloaded video to {video_file} and audio to {audio_file}")
        else:
            print(f"Failed to process {url}")

if __name__ == "__main__":
    video_urls = [
        "https://www.youtube.com/shorts/xMQTMK5AO_A",
        "https://www.youtube.com/shorts/9gUpMSnffFU"
    ]
    
    process_videos(video_urls)
