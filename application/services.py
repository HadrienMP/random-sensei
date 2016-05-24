# -*- coding: utf-8 -*-
import random
from application import hipchat_client
from config.sensei_gifs import *


WHO_ARE_YOU = ['who are you ?', 'Who are you ?', 'who are you?' 'Who are you ?']


def get_message(arguments_string=None, requester=None, room=None):
    
    if not room:
        return "Are you calling from another dimension ? I'm in hipchat where are you ?"
    
    if arguments_string in WHO_ARE_YOU:
        return "This is not the answer you seek little beetle"
    elif arguments_string == '':
        return _random_senseis_message(room, requester)
        

def _random_senseis_message(room, requester=None):
    senseis = hipchat_client.room_members(room)
    
    if len(senseis) < 2:
        return "Looks like you are going to have to be your own master..."
    
    senseis.remove(requester)
    picked_senseis = random.sample(senseis,2)
    
    message = "Your senseis for today are : @{} and @{}".format(*picked_senseis)
    
    if requester:
        message = "@" + requester + " " + message
    
    return message + '\n' + random.choice(FUNNY_GIFS)
