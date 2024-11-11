from parser import req
import telebot
from telebot import types
from dotenv import load_dotenv, find_dotenv
import os


file_path = "chart"
load_dotenv(find_dotenv())
token = os.getenv('token')
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])

def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Отримати текст", callback_data="send_text")
    markup.add(button)

    bot.send_message(message.chat.id, "Натисни кнопку, щоб отримати текст:", reply_markup=markup)

max_len_message = 4096

def handle_callback(call):
    if call.data == "send_text":
            with open(file_path, 'rb') as file:
                text = file.read()
            for item in range(0, len(text), max_len_message):
                bot.send_message(call.message.chat.id, text[item:item+max_len_message])

@bot.callback_query_handler(func=None)
def callback_handler(call):
    handle_callback(call)

req()
bot.polling(none_stop=True)
