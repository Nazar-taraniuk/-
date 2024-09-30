import telebot
token = "8133132609:AAEuD5LhCMzC4ErS1OrepzjSUMuR58f3674"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
     bot.infinity_polling()


