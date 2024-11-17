import telebot
from telebot import types
from config import get_token
from parser import req_apple, req_itunes
from decorators import log_message


def main():
    bot = telebot.TeleBot(get_token())
    url_apple = "https://kworb.net/apple_songs/index.html"
    url_itunes = "https://kworb.net/ww/"
    req_apple(url=url_apple)
    req_itunes(url=url_itunes)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        markup = types.InlineKeyboardMarkup()

        button_chart = types.InlineKeyboardButton("Отримати чарт apple", callback_data="send_text_chart")
        button_chart_itunes = types.InlineKeyboardButton("Отримати чарт itunes",
                                                         callback_data="send_text_chart_itunes")

        markup.add(button_chart, button_chart_itunes)

        bot.send_message(message.chat.id, "Натисніть кнопку, щоб отримати текст із відповідного файлу:",
                         reply_markup=markup)

    @log_message
    @bot.callback_query_handler(func=None)
    def handle_callback(call):
        max_len_message = 4096
        file_path = "chart" if call.data == "send_text_chart" else "chart_itunes"

        with open(file_path, 'rb') as file:
                text = file.read()
        for item in range(0, len(text), max_len_message):
                bot.send_message(call.message.chat.id, text[item:item + max_len_message])


        handle_start(call.message)
    print("bot ready")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
