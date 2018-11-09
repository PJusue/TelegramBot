import telebot
import requests
import json
import os
import subprocess
from sys import platform
url='http://api.telegram.org/bot659523754:AAFttt6Qf-Oz8Vtg7B5XPiBnDvh9X8BIPiQ/getUpdates'
chat_id=0
bot=telebot.TeleBot(token='659523754:AAFttt6Qf-Oz8Vtg7B5XPiBnDvh9X8BIPiQ')



@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id=message.chat.id
    user_name=message.chat.first_name
    welcome="hello "+user_name
    bot.send_message(chat_id,welcome)
@bot.message_handler(commands=['echo'])
def echo_message(message):
    bot.reply_to(message,message.text)
@bot.message_handler(commands=['stop'])
def send_goodbye(message):
    chat_id=message.chat.id
    bot.send_message(chat_id,"Bye")
@bot.message_handler(commands=['ipconfig'])
def send_ipInfo(message):
    if platform=="win32":
        chat_id=message.chat.id
        response=subprocess.Popen("ipconfig",shell=True,stdout=subprocess.PIPE).stdout
        bot.send_message(chat_id,response.read())
        pass
    elif platform=="linux" or platform=="linux2":
        chat_id=message.chat.id
        response=subprocess.Popen("ifconfig",shell=True,stdout=subprocess.PIPE).stdout
        bot.send_message(chat_id,response.read())
        pass

bot.polling()

