# -*- coding: utf-8 -*-
import re

COMMAND = r'[^ ]+'
ARGUMENTS = r'(.*)'
ARGUMENT_REGEX = r'^/' + COMMAND + '(\s+' + ARGUMENTS + r')?\s*$'
NUMBER_OF_SENSEI_REGEX = r'^\s*\d+\s*$'
EXCLUSION_REGEX = r'^(--without|-w)$'


def from_command(command):
    arguments = Arguments()

    m = re.search(ARGUMENT_REGEX, command)
    if not m:
        raise SenseiCommandException("This is not a valid sensei command")

    elif m.group(2):
        arguments_strings = re.split(r'\s+', m.group(2))

        arguments.number_of_senseis = get_number_of_senseis(arguments_strings)
        arguments.manual = is_manual_asked(arguments_strings)
        arguments.excluded_senseis = get_exclusions(arguments_strings)

    return arguments


def get_number_of_senseis(arguments_strings):
    if re.match(NUMBER_OF_SENSEI_REGEX, arguments_strings[0]):
        return int(arguments_strings[0].strip())
    else:
        return 2


def is_manual_asked(arguments_strings):
    return "-h" in arguments_strings or "--help" in arguments_strings


def get_exclusions(arguments_strings):
    excluded_senseis = list()

    add_to_exclusions = False
    for argument_string in arguments_strings:
        if add_to_exclusions:
            excluded_senseis.append(argument_string.replace('@', ''))
        else:
            add_to_exclusions = re.match(EXCLUSION_REGEX, argument_string)

    return excluded_senseis


class Arguments:
    def __init__(self):
        self.number_of_senseis = 2
        self.excluded_senseis = list()
        self.manual = False


class SenseiCommandException(Exception):
    pass
