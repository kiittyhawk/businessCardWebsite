import telebot

token = ''
bot = telebot.TeleBot(token)
my_id = 000


def send_message(text):
    bot.send_message(my_id, text)
