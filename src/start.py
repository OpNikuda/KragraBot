from main_func import get_greeting, get_markup
from logger import bot_logger


@bot_logger("bot_actions.log")
def bot_send_message(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            get_greeting(),
            reply_markup=get_markup()
        )


@bot_logger("bot_actions.log")
def bot_send_photo(bot):
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        channel_id = "@kragra"
        sender = f"@{message.from_user.username}" if message.from_user.username else f"ID:{message.from_user.id}"

        bot.send_photo(
            channel_id,
            message.photo[-1].file_id
        )
        bot.reply_to(message, "✅ Мем отправлен в Крадоград!")


