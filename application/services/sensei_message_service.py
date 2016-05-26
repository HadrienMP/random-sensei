# -*- coding: utf-8 -*-
import random

from application.services import hipchat_client
from config.sensei_gifs import *


def random_senseis_message(room, number_of_senseis=2, requester=None):

    senseis = hipchat_client.get_room_members(room)
    picked_senseis = _pick_random_senseis(senseis=senseis, number_of_senseis=number_of_senseis, requester=requester)

    message = _build_message(senseis, picked_senseis)

    requester_prefix = _get_requester_prefix(requester)
    message = requester_prefix + message
    message += _gif()

    return message


def _pick_random_senseis(senseis, number_of_senseis=2, requester=None):
    if requester:
        senseis.remove(requester)

    if len(senseis) == 0 or number_of_senseis <= 0:
        return list()
    elif len(senseis) <= number_of_senseis:
        return senseis
    else:
        return random.sample(senseis, number_of_senseis)


def _build_message(senseis, picked_senseis):
    if len(picked_senseis) == 0:
        message = "Looks like you are going to have to be your own master..."
    elif len(picked_senseis) == len(senseis):
        message = "You want @all to be your senseis ?"
    else:
        message = "Your senseis for today are : " + ' and '.join(['@' + sensei_name for sensei_name in picked_senseis])
    return message


def _gif():
    return '\n' + random.choice(SENSEI_GIFS)


def _get_requester_prefix(requester):
    if requester:
        return "@" + requester + " "
    return ''
