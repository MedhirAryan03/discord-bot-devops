import random
from data import top_movies, top_tracks
def generate_movie_question(movie, question_type):
    if question_type == 'year':
        question = f"What year was the movie '{movie['title']}' released?"
        options = [str(movie['year']), str(movie['year'] - random.randint(1, 5)), str(movie['year'] + random.randint(1, 5)), str(random.randint(1900, 2022))]
        random.shuffle(options)
        answer = str(movie['year'])
    elif question_type == 'actor':
        question = f"Who starred in the movie '{movie['title']}'?"
        options = [movie['actor'], random.choice([m['actor'] for m in top_movies if m['actor'] != movie['actor']]), random.choice([m['actor'] for m in top_movies]), random.choice([m['actor'] for m in top_movies])]
        random.shuffle(options)
        answer = movie['actor']
    elif question_type == 'director':
        question = f"Who directed the movie '{movie['title']}'?"
        options = [movie['director'], random.choice([m['director'] for m in top_movies if m['director'] != movie['director']]), random.choice([m['director'] for m in top_movies]), random.choice([m['director'] for m in top_movies])]
        random.shuffle(options)
        answer = movie['director']
    elif question_type == 'genre':
        question = f"What genre does the movie '{movie['title']}' belong to?"
        options = [movie['genre'], random.choice([m['genre'] for m in top_movies if m['genre'] != movie['genre']]), random.choice([m['genre'] for m in top_movies]), random.choice([m['genre'] for m in top_movies])]
        random.shuffle(options)
        answer = movie['genre']
    elif question_type == 'rating':
        question = f"What is the IMDb rating of the movie '{movie['title']}'?"
        options = [str(movie['rating']), str(round(movie['rating'] - random.uniform(0.5, 1.5), 1)), str(round(movie['rating'] + random.uniform(0.5, 1.5), 1)), str(round(random.uniform(0, 10), 1))]
        random.shuffle(options)
        answer = str(movie['rating'])
    return question, options, answer