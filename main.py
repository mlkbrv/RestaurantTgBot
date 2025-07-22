import os
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,f"Hello {message.from_user.username}")

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id,"<b>Help</b> <u>Information</u>",parse_mode='html')

@bot.message_handler(content_types=['github'])
def github(message):
    bot.reply_to(message,f"https://github.com/mlkbrv")

@bot.message_handler()
def temp(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, f"Hello {message.from_user.username}")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID {message.from_user.id}")

bot.polling(none_stop=True)