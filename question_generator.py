import random
from data import top_movies, top_tracks
from movie_choice import generate_movie_question
from music_choice import generate_music_question
def generate_movie_questions(num_questions):
    movie_questions = []
    for _ in range(num_questions):
        movie = random.choice(top_movies)
        question_type = random.choice(['year', 'actor', 'director', 'genre', 'rating'])
        question, options, answer = generate_movie_question(movie, question_type)
        movie_questions.append({'question': question, 'options': options, 'answer': answer})
    return movie_questions

def generate_music_questions(num_questions):
    music_questions = []
    for _ in range(num_questions):
        track = random.choice(top_tracks)
        question_type = random.choice(['year', 'singer', 'genre', 'rating'])
        question, options, answer = generate_music_question(track, question_type)
        music_questions.append({'question': question, 'options': options, 'answer': answer})
    return music_questions
