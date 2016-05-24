# -*- coding: utf-8 -*-
import evenly_distributed_picker
import random

SENSEIS = [
    {'name': 'Thomas', 'times_picked': 0},
    {'name': 'Raphaël', 'times_picked': 0},
    {'name': 'Céline', 'times_picked': 0},
    {'name': 'Ali', 'times_picked': 0},
    {'name': 'Hadrien', 'times_picked': 0},
]
FUNNY_GIFS = [
    "http://45.media.tumblr.com/c055bc68805f88771faf825b901e9bcc/tumblr_nvrrypkvaK1ubyc4yo6_500.gif",
    "https://media.giphy.com/media/qJVCvxP2kC3EQ/giphy.gif",
    "http://i.giphy.com/IDAHKQVpqDeKs.gif",
    "http://i.giphy.com/FckDucw9RHfZC.gif",
    "http://i.giphy.com/Zfws1JEW4A4LK.gif",
    "http://i.giphy.com/cMCgTNveyUhMY.gif"
]
WHO_ARE_YOU = ['who are you ?', 'Who are you ?', 'who are you?' 'Who are you ?']


def get_message(arguments_string, requester=None):
    
    if arguments_string in WHO_ARE_YOU:
        return "This is not the answer you seek little beetle"
    elif arguments_string == '':
        return _random_senseis_message(requester)
        

def _random_senseis_message(requester=None):
    picked_senseis = random.sample(SENSEIS,2)
        
    senseis_names = list()
    for sensei in picked_senseis:
        senseis_names.append(sensei['name'])
        sensei['times_picked'] += 1
        
    
    message = "Your senseis for today are : {} and {}".format(*senseis_names)
    
    if requester:
        message = "@" + requester + " " + message
    
    return message + '\n' + random.choice(FUNNY_GIFS)
