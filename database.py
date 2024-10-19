import sqlite3

DATABASE_NAME = "foresthacks.db"

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE_NAME)

def setup_db():
    """Set up the database with the required tables."""
    with connect_db() as conn:
        cursor = conn.cursor()
        
        # Table for storing video details
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
        
        # Table for storing user details
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        
        # Table for storing watch history
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS watch_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                video_id INTEGER,
                reaction INTEGER DEFAULT 0,  -- -1: dislike, 0: no reaction, 1: like
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(video_id) REFERENCES videos(id)
            )
        ''')
        
        # Table for storing user preferences
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS preferences (
                user_id INTEGER PRIMARY KEY,
                math REAL DEFAULT 0.25,
                science REAL DEFAULT 0.25,
                english REAL DEFAULT 0.25,
                history REAL DEFAULT 0.25,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        
        conn.commit()
    print("Database setup complete.")

# Example of adding a video entry
def add_video(youtube_url, video_file_path, audio_file_path, tags="", transcript=""):
    """Add a new video entry to the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO videos (youtube_url, video_file_path, audio_file_path, tags, transcript)
            VALUES (?, ?, ?, ?, ?)
        ''', (youtube_url, video_file_path, audio_file_path, tags, transcript))
        conn.commit()
    print(f"Added video: {youtube_url}")

def get_all_videos():
    """Retrieve all video entries from the database."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM videos')
        videos = cursor.fetchall()
    return videos
