from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_greeting():
    return (
        "Привет, я бот Крадограда!\n"
        "Скидывай сюда свои мемчики, но помни!\n"
        "Я не просто пересылаю, я ещё и стучу. Шли контент, если готов к последствиям. 🚔"
    )

def get_markup():
    markup = InlineKeyboardMarkup()
    btn1 = (InlineKeyboardButton('Отправить мем', callback_data='send_meme'))
    btn2 = (InlineKeyboardButton('Назад', callback_data='back'))
    markup.add(btn1, btn2)

    return markup

