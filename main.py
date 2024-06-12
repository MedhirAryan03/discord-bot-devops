import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from question_generator import generate_movie_questions, generate_music_questions
from answer_evaluator import evaluate_answers

# Load environment variables
load_dotenv() 

# Fetch the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the intents
intents = discord.Intents.default()

# Create the client instance
client = commands.Bot(command_prefix='!', intents=intents)

class QuizSession:
    def __init__(self, channel):
        self.channel = channel
        self.asked_movie = False
        self.asked_music = False
        self.movie_question = None
        self.music_question = None

    async def start(self):
        await self.channel.send('Welcome to the Quiz! Get ready to test your knowledge.\nDo you want a movie question or a music question? Type `movie` or `music`.')

    async def ask_movie_question(self):
        self.asked_movie = True
        # Generate a movie question
        self.movie_question = generate_movie_questions(1)[0]

        await self.channel.send(self.movie_question['question'])
        await self.channel.send('\n'.join([f"{index+1}. {option}" for index, option in enumerate(self.movie_question['options'])]))
        await self.channel.send("Please type the number of your answer.")

    async def ask_music_question(self):
        self.asked_music = True
        # Generate a music question
        self.music_question = generate_music_questions(1)[0]

        await self.channel.send(self.music_question['question'])
        await self.channel.send('\n'.join([f"{index+1}. {option}" for index, option in enumerate(self.music_question['options'])]))
        await self.channel.send("Please type the number of your answer.")

    async def evaluate_answer(self, user_answer):
        if self.asked_movie:
            correct_answers = evaluate_answers([self.movie_question], [user_answer])
            await self.channel.send(f"Your answer for the movie question is {'correct' if correct_answers == 1 else 'incorrect'}!")
        elif self.asked_music:
            correct_answers = evaluate_answers([self.music_question], [user_answer])
            await self.channel.send(f"Your answer for the music question is {'correct' if correct_answers == 1 else 'incorrect'}!")

# Dictionary to store quiz sessions by channel ID
quiz_sessions = {}

@client.event
async def on_ready():
    print(f'{client.user} is ready to start')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    session = quiz_sessions.get(message.channel.id)
    if session:
        if not session.asked_movie and message.content.lower() == 'movie':
            await session.ask_movie_question()
        elif not session.asked_music and message.content.lower() == 'music':
            await session.ask_music_question()
        else:
            await session.evaluate_answer(message.content.strip())
    elif message.content.startswith('!startquiz'):
        quiz_sessions[message.channel.id] = QuizSession(message.channel)
        await quiz_sessions[message.channel.id].start()
    else:
        await message.channel.send("No quiz session is currently active. Start a quiz session using `!startquiz`.")

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()
