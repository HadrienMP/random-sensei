# -*- coding: utf-8 -*-
import re

from application.services.sensei_message_service import *

WHO_ARE_YOU = ['who are you ?', 'Who are you ?', 'who are you?' 'Who are you ?']


def build_message(room, arguments_string=None, requester=None):
    if arguments_string in WHO_ARE_YOU:
        return "This is not the answer you seek little beetle"
    elif arguments_string == '':
        return random_senseis_message(room, requester=requester)
    elif re.match(r'^\d+$', arguments_string):
        return random_senseis_message(room, requester=requester, number_of_senseis=int(arguments_string))
