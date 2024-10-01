import sqlite3

DATABASE_NAME = "foresthacks.db"

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)

def setup_db():
    """Set up the database with the required table."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                youtube_url TEXT NOT NULL,
                video_file_path TEXT NOT NULL,
                audio_file_path TEXT NOT NULL,
                tags TEXT,
                transcript TEXT
            )
        ''')
        conn.commit()
    print("Database setup complete.")

def add_video(youtube_url, file_path, tags="", transcript=""):
    """Add a new video entry to the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO videos (youtube_url, file_path, tags, transcript)
            VALUES (?, ?, ?, ?)
        ''', (youtube_url, file_path, tags, transcript))
        conn.commit()
    print(f"Added video: {youtube_url}")

def get_all_videos():
    """Retrieve all video entries from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM videos')
        videos = cursor.fetchall()
    return videos
