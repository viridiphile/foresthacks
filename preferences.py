import random
import sqlite3

DATABASE_NAME = "foresthacks.db"

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def get_user_preferences(user_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT math, science, english, history FROM preferences WHERE user_id=?', (user_id,))
        return cursor.fetchone()

def recommend_video(user_id):
    preferences = get_user_preferences(user_id)
    categories = ['math', 'science', 'english', 'history']
    chosen_category = random.choices(categories, weights=preferences, k=1)[0]

    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, title, youtube_url FROM videos 
            WHERE tags LIKE ? AND id NOT IN (SELECT video_id FROM watch_history WHERE user_id=? AND reaction=-1)
            ORDER BY RANDOM() LIMIT 1
        ''', (f'%{chosen_category}%', user_id))
        return cursor.fetchone()

def update_preferences(user_id, category, reaction):
    with connect_db() as conn:
        cursor = conn.cursor()
        if reaction == 1:
            cursor.execute(f'UPDATE preferences SET {category} = {category} + 0.05 WHERE user_id=?', (user_id,))
        elif reaction == -1:
            cursor.execute(f'UPDATE preferences SET {category} = {category} - 0.1 WHERE user_id=?', (user_id,))

        cursor.execute('SELECT math, science, english, history FROM preferences WHERE user_id=?', (user_id,))
        prefs = cursor.fetchone()
        total = sum(prefs)
        normalized_prefs = [p / total for p in prefs]

        cursor.execute('''
            UPDATE preferences
            SET math=?, science=?, english=?, history=?
            WHERE user_id=?
        ''', (*normalized_prefs, user_id))
        conn.commit()
