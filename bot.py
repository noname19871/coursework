# -*- coding: utf-8 -*-
import telebot
import os


token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(token)

admins = bot.get_chat_administrators()


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in admins:
        bot.send_message(message.chat.id, 'ты админ')
    else:
        bot.send_message(message.chat.id, 'ты не админ')


# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.polling(none_stop=True)
