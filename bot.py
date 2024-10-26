import telebot
from random import choice

TOKEN = ''  
masage = ['ГОЙДА Работает','ГОЙДА!!!','Поддержать СВОЮ ГОЙДУ','ГОЙДА Работает Братья ГОЙДА' , 'Работаем Братья Гоида']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напиши /гойда /Гойда /goida /гойда или /ГОЙДА для получения базы')

@bot.message_handler(commands=['Гойда', 'Goida', 'goida', 'гойда','ГОЙДА'])
def goida_message(message):
    bot.send_message(message.chat.id, choice(masage))

bot.polling()