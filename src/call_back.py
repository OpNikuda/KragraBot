from main_func import get_greeting, get_markup
from logger import bot_logger

@bot_logger("bot_actions.log")
def setup_callbacks(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'send_meme')
    def send_meme(call):
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "Просто отправь мне мем (фото) и я перешлю его в канал!"
        )

    @bot.callback_query_handler(func=lambda call: call.data == 'back')
    def back(call):
        bot.answer_callback_query(call.id)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=get_greeting(),
            reply_markup=get_markup()
        )

