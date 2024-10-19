import os
import whisper
from dotenv import load_dotenv
from video_downloader import download_youtube_video_and_audio
import database

load_dotenv()

# Setup the database
database.setup_db()

def transcribe_audio_with_whisper(audio_file):
    model = whisper.load_model("small")
    result = model.transcribe(audio_file)
    return result['text']

def process_videos(video_urls):
    for url in video_urls:
        print(f"Processing {url}...")
        
        # Download video and audio
        video_file, audio_file = download_youtube_video_and_audio(url)

        if video_file and audio_file:
            # Transcribe the audio
            transcript = transcribe_audio_with_whisper(audio_file)

            # Save the transcript
            transcript_file = f"{audio_file.split('.')[0]}_transcript.txt"
            with open(transcript_file, "w") as f:
                f.write(transcript)
            
            print(f"Transcription saved to {transcript_file}")
        else:
            print(f"Failed to process {url}")

if __name__ == "__main__":
    video_urls = [
        "https://www.youtube.com/shorts/xMQTMK5AO_A",
        "https://www.youtube.com/shorts/9gUpMSnffFU"
    ]
    
    process_videos(video_urls)
