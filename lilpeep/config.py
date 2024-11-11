from dotenv import load_dotenv, find_dotenv
import os
import telebot

load_dotenv(find_dotenv())
token = os.getenv('token')

if not token:
    raise ValueError("not .env")

bot = telebot.TeleBot(token)