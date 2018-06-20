# -*- coding: utf-8 -*-
import telebot
import os

token = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
     bot.polling(none_stop=True)
