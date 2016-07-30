# -*- coding: utf-8 -*-
import re

from application.services.sensei_message_service import *

WHO_ARE_YOU = ['who are you ?', 'Who are you ?', 'who are you?' 'Who are you ?']


def build_message(room, arguments, requester=None):
    return random_senseis_message(room,
                                  arguments.number_of_senseis,
                                  excluded_senseis=arguments.excluded_senseis,
                                  requester=requester)
