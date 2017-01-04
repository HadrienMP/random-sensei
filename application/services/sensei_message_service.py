# -*- coding: utf-8 -*-
import random

from application.services import hipchat_client
from config.sensei_gifs import *


def random_senseis_message(room, number_of_senseis, requester=None, excluded_senseis=list()):
    room_members = _get_room_members_without_requester(room, requester)
    senseis = _get_potential_senseis(room_members, excluded_senseis)
    picked_senseis = _pick_random_senseis(senseis=senseis, number_of_senseis=number_of_senseis)

    message = _build_message(room_members, picked_senseis)
    message = _address_message_to_requester(message, requester)
    message += _gif()

    return message


def _get_room_members_without_requester(room, requester=None):
    room_members = hipchat_client.get_room_members(room)
    if requester and requester in room_members:
        room_members.remove(requester)

    return room_members


def _get_potential_senseis(room_members, excluded_senseis):
    return [sensei for sensei in room_members if sensei not in excluded_senseis]


def _pick_random_senseis(senseis, number_of_senseis):
    if len(senseis) == 0 or number_of_senseis <= 0:
        return list()
    elif len(senseis) <= number_of_senseis:
        return senseis
    else:
        return random.sample(senseis, number_of_senseis)


def _build_message(room_members, picked_senseis):
    if len(picked_senseis) == 0:
        message = "Looks like you are going to have to be your own master..."
    elif len(picked_senseis) == len(room_members):
        message = "Do you want @all to be your senseis ?"
    else:
        message = "Your senseis are : " + ' and '.join(['@' + sensei_name for sensei_name in picked_senseis])
    return message


def _address_message_to_requester(message, requester=None):
    requester_prefix = _get_requester_prefix(requester)
    message = requester_prefix + message
    return message


def _get_requester_prefix(requester):
    if requester:
        return "@" + requester + " "
    return ''


def _gif():
    return '\n' + random.choice(SENSEI_GIFS)
