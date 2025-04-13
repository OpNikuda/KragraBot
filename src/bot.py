from logger import bot_logger
import threading

@bot_logger("bot_errors.log")
def run_bot():
    import telebot
    from config import your_token
    from start import bot_send_message, bot_send_photo
    from call_back import setup_callbacks

    bot = telebot.TeleBot(your_token)

    bot_send_message(bot)
    bot_send_photo(bot)
    setup_callbacks(bot)

    threading.Thread(target=bot.polling, kwargs={'none_stop': True}).start()

if __name__ == "__main__":
    run_bot()

