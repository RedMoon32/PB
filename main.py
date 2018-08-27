from os import environ
import os
from telethon import TelegramClient, events
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.sync import TelegramClient
import socks
from telethon.sessions import StringSession
from configs import *
from telethon.tl.functions.channels import InviteToChannelRequest


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


def add_people_to_group(client, guest_phone_number, group_id):
    contact = InputPhoneContact(client_id=0, phone=guest_phone_number, first_name="Name ",
                                last_name="Last_name")
    result = client(ImportContactsRequest([contact]))
    res = client.get_entity(group_id)
    print(res)
    # client(AddChatUserRequest(user_id=result.users[0], fwd_limit=0, chat_id=group_id))
    client(InviteToChannelRequest(res, [result.users[0]]))


def add_phone_numbers(phones):
    users = load_sessions()
    userid = 0
    num = 0
    while num < len(phones):
        try:
            with TelegramClient(StringSession(users[userid]), api_id, hash) as client:
                print(client.get_entity(groupd_id))
                add_people_to_group(client, phones[num], groupd_id)
                num += 1
                if num % 60 == 0:
                    userid += 1
                    continue
        except Exception as e:
            print(str(e))


def number_exists(phone):
    try:
        users = load_sessions()
        with TelegramClient(StringSession(users[0]), api_id, hash) as client:
            print(client.get_entity(phone))
        return True
    except:
        return False


if __name__ == '__main__':
    # number_exists('+79279348579')
    # add_new_session()
    add_phone_numbers(['+79174299995'])
    # while True:
    #    add_new_session()
