from config import bot
from handlers import handle_start, callback_handler
from parser import req

req()

if __name__ == "__main__":
    print("bot ready")
    bot.polling(none_stop=True)