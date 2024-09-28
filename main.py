import os
import pytube
import whisper
import ffmpeg
from dotenv import load_dotenv


api_key = os.getenv("YOUTUBE_API_KEY")

if not api_key:
    raise ValueError("Missing YOUTUBE_API_KEY environment variable")

def download_youtube_video_as_audio(youtube_url, output_path="audio.mp3"):
    yt = pytube.YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(filename="video.mp4")
    
    # Convert video to audio using ffmpeg
    os.system(f"ffmpeg -i video.mp4 -q:a 0 -map a {output_path}")
    print(f"Audio saved as {output_path}")
    return output_path

def transcribe_audio_with_whisper(audio_file):
    model = whisper.load_model("small")  # Use "base" model, you can also try "small", "medium", "large"
    result = model.transcribe(audio_file)
    return result['text']

if __name__ == "__main__":
    # Step 1: Download the YouTube video as audio
    youtube_url = "https://youtube.com/shorts/xMQTMK5AO_A?si=LysnH_0J883qEzh6" #Long devision 
    audio_file = download_youtube_video_as_audio(youtube_url)

    # Step 2: Transcribe the audio
    transcript = transcribe_audio_with_whisper(audio_file)
    
    # Step 3: Save the transcript to a file
    with open("transcript.txt", "w") as f:
        f.write(transcript)
    
    print("Transcription complete. Transcript saved to 'transcript.txt'")
