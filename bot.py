# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler
from configs import *
from telegram.ext import Filters
from main import *


class TBot:

    def __init__(self):
        self.updater = Updater(token, request_kwargs={'proxy_url': 'socks5://54.37.234.65:8081/'}

                               )
        self.bot = self.updater.bot
        self.add_handlers()
        self.updater.start_polling()

    def add_handlers(self):
        map = [MessageHandler(Filters.document, self.get_file)]
        for i in map:
            self.updater.dispatcher.add_handler(i)

    def get_file(self, bot, update):
        print(update)
        file_id = update.message.document.file_id
        newFile = bot.get_file(file_id)
        newFile.download('numbers.txt')
        ph = []
        for i in open('numbers.txt', 'r'):
            i = i.strip()
            i = i.replace(' ', '')
            i = i.replace('-', '')
            ph += [i]
        add_phone_numbers(phones=ph)
        # add_phone_numbers('numbers.txt')


def main():
    b = TBot()


if (__name__ == "__main__"):
    main()
