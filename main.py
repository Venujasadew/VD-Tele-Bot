import os
import telebot


bot = telebot.TeleBot("1969051592:AAFtyw2lD0u8K9EA5Pm3qp4_pOXiJ9MAoJg")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm VndGroup Chat Bot 📌Made by https://t.me/Venuja_Sadew")


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")



bot.polling()