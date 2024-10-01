import os
import pytube
import whisper
import ffmpeg
from dotenv import load_dotenv

# Load env variables
load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")

if not api_key:
    raise ValueError("Missing YOUTUBE_API_KEY environment variable")

def download_youtube_video_as_audio(youtube_url, output_path="audio.mp3"):
    yt = pytube.YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(filename="video.mp4")
    
    # Convert video to audio w/ffmpeg
    os.system(f"ffmpeg -i video.mp4 -q:a 0 -map a {output_path}")
    print(f"Audio saved as {output_path}")
    return output_path

def transcribe_audio_with_whisper(audio_file):
    model = whisper.load_model("small")  
    result = model.transcribe(audio_file)
    return result['text']

if __name__ == "__main__":
    # 1. Download the YouTube video as audio
    youtube_url = "https://youtu.be/SLze82Zcc4Y" 
    try:
        audio_file = download_youtube_video_as_audio(youtube_url)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1) 

    # 2. Transcribe the audio
    transcript = transcribe_audio_with_whisper(audio_file)
    
    # 3. Save the transcript to a file
    with open("transcript.txt", "w") as f:
        f.write(transcript)
    
    print("Transcription complete. Transcript saved to 'transcript.txt'")

