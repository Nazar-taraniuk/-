from telebot import types
from config import bot
from decorators import log_message

file_path = "chart"

max_len_message = 4096

@log_message
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Отримати текст", callback_data="send_text")
    markup.add(button)

    bot.send_message(message.chat.id, "Натисни кнопку, щоб отримати текст:", reply_markup=markup)

def handle_callback(call):
    if call.data == "send_text":
            with open(file_path, 'rb') as file:
                text = file.read()
            for item in range(0, len(text), max_len_message):
                bot.send_message(call.message.chat.id, text[item:item+max_len_message])

@bot.message_handler(commands=['start'])
def handle_start(message):
    start(message)

@bot.callback_query_handler(func=None)
def callback_handler(call):
    handle_callback(call)
