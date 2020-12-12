import os
import sys
import subprocess
import telebot
import time
#pip3 install pytelegrambotapi --upgrade



bot = telebot.TeleBot('1269788895:AAG3pFUfu4MIFr86iDI9K6xQAKbn1ozJ914')

board = list(range(1,10))

def draw_board(bot,message,board):
    bot.send_message(message.from_user.id, "-" * 13)
    for i in range(3):
        bot.send_message(message.from_user.id,"|"+ str(board[0+i*3])+ "|"+ str(board[1+i*3])+ "|"+ str(board[2+i*3])+ "|")
        bot.send_message(message.from_user.id, "-" * 13)   
def take_input(bot,message,player_token):
    valid = False
    while not valid:
        valid = True
        #bot.send_message(message.from_user.id,"Куда поставим " + player_token+"? ")
        player_answer = message.text
        try:
            player_answer = int(player_answer)
        except:
            bot.send_message(message.from_user.id,"Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                bot.send_message(message.from_user.id,"Эта клеточка уже занята")
        else:
            bot.send_message(message.from_user.id,"Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


stateGame = 0
# 0 no game
# 1 start game and write board
# 2 insert data to board
countGame = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global stateGame
    global countGame
    print(stateGame)
    print(countGame)
    if message.text == "/help":
        bot.send_message(message.from_user.id, "hello my dear  hoziain im a you slav")
    elif stateGame == 0 and message.text == "gogo":
        stateGame = 1
        countGame = 0
        draw_board(bot,message,board)
    elif stateGame >= 1 and message.text.isdigit():
        stateGame = 2
        if countGame % 2 == 0:
            take_input(bot,message,"X")
        else:
            take_input(bot,message,"O")        
        countGame += 1
        if countGame > 4:
            tmp = check_win(board)
            if tmp:
                bot.send_message(message.from_user.id, tmp)
                bot.send_message(message.from_user.id, "выиграл!")
                win = True
                stateGame = 0
        if countGame == 9:
            bot.send_message(message.from_user.id,"Ничья!")
            stateGame = 0
        draw_board(bot,message,board)
    elif message.text == "tt":
        draw_board(bot,message,board)
    elif "aa" in message.text:
        take_input(bot,message,"X")
    else:
        stateGame = 0
        bot.send_message(message.from_user.id, "i undestend write /help.")

bot.polling(none_stop=True, interval=0)	
