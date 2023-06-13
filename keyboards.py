from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from configs import LANGUAGES


def generate_languages():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for language in LANGUAGES.values():
        btn = KeyboardButton(text=language)
        buttons.append(btn)
    markup.add(*buttons)
    return markup