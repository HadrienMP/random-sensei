# -*- coding: utf-8 -*-
import re


ARGUMENT_REGEX = r'/[^ ]+\s+(.*)\s*'
NUMBER_OF_SENSEI_REGEX = r'^\s*\d+\s*$'
EXCLUSION_REGEX = r'^\s*-@?([^ ]+)\s*$'


def from_command(command):
    arguments = Arguments()

    # TODO lancer une exception si la commande ne matche pas le format attendu
    m = re.search(ARGUMENT_REGEX, command)
    if m:
        arguments_strings = m.group(1).split(" ")

        arguments.number_of_senseis = get_number_of_senseis(arguments_strings)
        arguments.excluded_senseis = get_exclusions(arguments_strings)

    return arguments


def get_number_of_senseis(arguments_strings):
    if re.match(NUMBER_OF_SENSEI_REGEX, arguments_strings[0]):
        return int(arguments_strings[0].strip())
    else:
        return 2


def get_exclusions(arguments_strings):
    excluded_senseis = list()

    for argument_string in arguments_strings:
        m = re.search(EXCLUSION_REGEX, argument_string)
        if m:
            excluded_senseis.append(m.group(1))

    return excluded_senseis


class Arguments:
    def __init__(self):
        self.number_of_senseis = 2
        self.excluded_senseis = list()
