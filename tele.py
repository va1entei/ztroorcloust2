import os
import sys
import subprocess
import telebot
import time
#pip3 install pytelegrambotapi --upgrade

bot = telebot.TeleBot('1269788895:AAG3pFUfu4MIFr86iDI9K6xQAKbn1ozJ914')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == "/help":
        bot.send_message(message.from_user.id, "i am stupit")
    else:
        bot.send_message(message.from_user.id, "i undestend write /help.")

bot.polling(none_stop=True, interval=0)	
