import random
from data import top_movies, top_tracks

def generate_music_question(track, question_type):
    if question_type == 'year':
        question = f"What year was the song '{track['title']}' released?"
        options = [str(track['year']), str(track['year'] - random.randint(1, 5)), str(track['year'] + random.randint(1, 5)), str(random.randint(1900, 2022))]
        random.shuffle(options)
        answer = str(track['year'])
    elif question_type == 'singer':
        question = f"Who performed the song '{track['title']}'?"
        options = [track['singer'], random.choice([t['singer'] for t in top_tracks if t['singer'] != track['singer']]), random.choice([t['singer'] for t in top_tracks]), random.choice([t['singer'] for t in top_tracks])]
        random.shuffle(options)
        answer = track['singer']
    elif question_type == 'genre':
        question = f"What genre does the song '{track['title']}' belong to?"
        options = [track['genre'], random.choice([t['genre'] for t in top_tracks if t['genre'] != track['genre']]), random.choice([t['genre'] for t in top_tracks]), random.choice([t['genre'] for t in top_tracks])]
        random.shuffle(options)
        answer = track['genre']
    elif question_type == 'rating':
        question = f"What is the rating of the song '{track['title']}'?"
        options = [str(track['rating']), str(round(track['rating'] - random.uniform(0.5, 1.5), 1)), str(round(track['rating'] + random.uniform(0.5, 1.5), 1)), str(round(random.uniform(0, 10), 1))]
        random.shuffle(options)
        answer = str(track['rating'])
    return question, options, answer