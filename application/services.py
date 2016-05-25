# -*- coding: utf-8 -*-
import random
from application import hipchat_client
from config.sensei_gifs import *
import re


WHO_ARE_YOU = ['who are you ?', 'Who are you ?', 'who are you?' 'Who are you ?']


def get_message(arguments_string=None, requester=None, room=None):
    
    if not room:
        return "Are you calling from another dimension ? I'm in hipchat where are you ?"
    
    if arguments_string in WHO_ARE_YOU:
        return "This is not the answer you seek little beetle"
    elif arguments_string == '':
        return _random_senseis_message(room, requester)
    elif re.match(r'^\d+$', arguments_string):
        return _random_senseis_message(room, requester=requester, number_of_senseis=int(arguments_string))
        

def _random_senseis_message(room, requester=None, number_of_senseis=2):
    senseis = hipchat_client.room_members(room)
    
    if requester:
        senseis.remove(requester)
    
    if len(senseis) == 0 or number_of_senseis <= 0:
        message = "Looks like you are going to have to be your own master..."
    elif len(senseis) <= number_of_senseis:
        message = "You want @all to be your senseis ?"
    else:
        picked_senseis = random.sample(senseis,number_of_senseis)
        message = "Your senseis for today are : " + ' and '.join(['@' + sensei_name for sensei_name in picked_senseis])
    
    if requester:
        message = "@" + requester + " " + message
    
    return message + '\n' + random.choice(SENSEI_GIFS)


def _pick_random_senseis(senseis, number_of_senseis=2, requester=None):
    if requester:
        senseis.remove(requester)

    if len(senseis) == 0 or number_of_senseis <= 0:
        return list()
    elif len(senseis) <= number_of_senseis:
        return senseis
    else:
        return random.sample(senseis, number_of_senseis)
