import os
import sys
import subprocess
import telebot
import time
#pip3 install pytelegrambotapi --upgrade

board = list(range(1,10))



bot = telebot.TeleBot('1269788895:AAG3pFUfu4MIFr86iDI9K6xQAKbn1ozJ914')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == "/help":
        bot.send_message(message.from_user.id, "hello my dear  hoziain im a you slav")
    elif message.text == "tt":
        board = list(range(1,10))
        bot.send_message(message.from_user.id, "-" * 13)
        for i in range(3):
            bot.send_message(message.from_user.id,"|"+ str(board[0+i*3])+ "|"+ str(board[1+i*3])+ "|"+ str(board[2+i*3])+ "|")
            bot.send_message(message.from_user.id, "-" * 13)           

    else:
        bot.send_message(message.from_user.id, "i undestend write /help.")

bot.polling(none_stop=True, interval=0)	
