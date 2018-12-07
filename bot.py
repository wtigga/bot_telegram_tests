# -*- coding: utf-8 -*-

import os
import telebot

# TOKEN = os.environ.get('TOKEN')
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
bot = telebot.AsyncTeleBot(TOKEN)


text_messages = {
    'welcome':
        u'Добро пожаловать, {name}!\n\n'
        u'Представьтесь, пожалуйста.\n',

    'info':
        u'Привет. Я робот.\n'
        u'Иди нахуй.\n',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}



@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    bot.reply_to(message, text_messages['info'])


@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)

    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)

    bot.reply_to(message, text_messages['welcome'].format(name=name))


@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")


def listener(messages):
    for m in messages:
        print(str(m))


if __name__ == '__main__':
    bot.polling(none_stop=True)