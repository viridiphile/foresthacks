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
    "https://www.youtube.com/shorts/9gUpMSnffFU",
    "https://www.youtube.com/shorts/lFPj_yKAeSU",
    "https://www.youtube.com/shorts/n0EDtZyTaiA",
    "https://www.youtube.com/shorts/Sz3jKlWf88E",
    "https://www.youtube.com/shorts/ddGS9yYratI",
    "https://www.youtube.com/shorts/0ru5bzh7p8I",
    "https://www.youtube.com/shorts/UhL9HPjWPmY",
    "https://www.youtube.com/shorts/G8ZYGwiIP2E",
    "https://www.youtube.com/shorts/ld4K5nw9gsk",
    "https://www.youtube.com/shorts/wrTsY1qnlQs",
    "https://www.youtube.com/shorts/BoFbNLrTSH8",
    "https://www.youtube.com/shorts/XgpwmUPOVqk",
    "https://www.youtube.com/shorts/0257ogtq7eQ",
    "https://www.youtube.com/shorts/1SO8BgloZog",
    "https://www.youtube.com/shorts/17VDCL-bABw",
    "https://www.youtube.com/shorts/o-3hQft09wM",
    "https://www.youtube.com/shorts/Kv2egxqjBo0",
    "https://www.youtube.com/shorts/xdapvCJqwT8",
    "https://www.youtube.com/shorts/cGtsY1hqUho",
    "https://www.youtube.com/shorts/tgGkeH3O4Ro",
    "https://www.youtube.com/shorts/NqrnUrwgsLo",
    ]
    
    process_videos(video_urls)