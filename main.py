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

@bot.message_handler(commands=['github'])
def github(message):
    bot.reply_to(message,f"https://github.com/mlkbrv")

@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Go to site",url="https://github.com/mlkbrv"))
    btn1 = telebot.types.InlineKeyboardButton("Delete Photo",callback_data="delete")
    btn2 = telebot.types.InlineKeyboardButton("ChangeText",callback_data="edit")
    markup.row(btn1,btn2)
    bot.reply_to(message, "Какое красивое фото", reply_markup=markup)

@bot.message_handler()
def temp(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, f"Hello {message.from_user.username}")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID {message.from_user.id}")

bot.remove_webhook()

bot.polling(none_stop=True)
