import telebot
from configs import *
from keyboards import *
from databases import *
from googletrans import Translator
import sqlite3
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'about_dev', 'history'])
def start_welcome(message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    if message.text == '/start':
        bot.send_message(chat_id, f"👨🏻‍💻 Hello {full_name}.\n🤖 I am English words translator bot.  I will help you translate your difficult words")
        start_translate(message)
    elif message.text == '/about_dev':
        bot.send_message(chat_id, f"""👨🏻‍💻 During the creation of this bot we used programing language python and ,odule pyTelegramBotAPI.
This bot created by back-end developer Alimovskiy.
t.me/ChaLa_HaCkeR""")
    elif message.text == '/history':
        pass

def start_translate(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f'From which language do you want to translate ?',
                     reply_markup=generate_languages())
    bot.register_next_step_handler(msg, second_language)    


def second_language(message):
    chat_id = message.chat.id
    src = message.text
    msg = bot.send_message(chat_id, f'To which language do you want to translate ?',
                     reply_markup=generate_languages())
    bot.register_next_step_handler(msg, give_text, src)


def give_text(message, src):
    chat_id = message.chat.id
    dest = message.text
    msg = bot.send_message(chat_id, f'Please write the text:')
    bot.register_next_step_handler(msg, translating, src, dest)

def translating(message, src, dest):
    chat_id = message.chat.id
    user_text = message.text

    translator = Translator()
    tr_text = translator.translate(src=get_key(src), dest=get_key(dest), text=user_text).text

    database = sqlite3.connect('translator.db')
    cursor = database.cursor()



bot.polling(non_stop=True)