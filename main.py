from os import environ
import os
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
import socks
from telethon.sessions import StringSession
from configs import *


def add_new_session():
    try:
        with TelegramClient(environ.get('TG_SESSION', 'session'), api_id, hash) as client:
            client.start()
            open('log.txt', 'a').write(StringSession.save(client.session) + '\n')
        os.remove('session.session')
    except:
        pass


def load_sessions():
    users = []
    for i in open('log.txt', 'r'):
        users.append(i.strip())
    return users


def number_exists(phone):
    try:
        users = load_sessions()
        with TelegramClient(StringSession(users[0]), api_id, hash) as client:
            print(client.get_entity(phone))
        return True
    except:
        return False


if __name__ == '__main__':
    number_exists('+7925558579')
    # while True:
    #    add_new_session()
