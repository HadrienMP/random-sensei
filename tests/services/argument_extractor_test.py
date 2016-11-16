# -*- coding: utf-8 -*-
from mock import Mock
import pytest

from application.services.argument_extractor import *

##############################################################################

# DEFAULT

##############################################################################

def test_should_use_default_arguments_when_absent():
    # TEST
    arguments = from_command('/random-sensei')

    # ASSERT
    assert arguments.number_of_senseis == 2
    assert len(arguments.excluded_senseis) == 0

##############################################################################

# NUMBER OF SENSEIS

##############################################################################

def test_should_return_number_of_senseis_when_present():
    # TEST
    arguments = from_command('/random-sensei  10      ')

    # ASSERT
    assert arguments.number_of_senseis == 10
    assert len(arguments.excluded_senseis) == 0


def test_should_extract_number_of_sensei_when_other_arguments_are_present_after():
    # TEST
    arguments = from_command('/randomA-sensei  8   test   ')

    # ASSERT
    assert arguments.number_of_senseis == 8
    assert len(arguments.excluded_senseis) == 0


def test_should_not_extract_number_of_sensei_when_other_arguments_are_present_before():
    # TEST
    arguments = from_command('/random-sensei test  140   ')

    # ASSERT
    assert arguments.number_of_senseis == 2
    assert len(arguments.excluded_senseis) == 0


##############################################################################

# EXCLUDED SENSEIS

##############################################################################

def test_should_extract_excluded_senseis():
    # TEST
    arguments = from_command('/random-sensei --without foo bar')

    # ASSERT
    assert arguments.excluded_senseis == ['foo', 'bar']


def test_should_extract_excluded_senseis_with_arobase():
    # TEST
    arguments = from_command('/random-sensei --without @foo')

    # ASSERT
    assert arguments.excluded_senseis == ['foo']


def test_should_exclude_even_weird_names():
    # TEST
    arguments = from_command('/random-sensei --without @[|{$ẑfgg')

    # ASSERT
    assert arguments.excluded_senseis == ['[|{$ẑfgg']


def test_should_extract_excluded_senseis_with_short_param_command():
    # TEST
    arguments = from_command('/random-sensei -w foo bar')

    # ASSERT
    assert arguments.excluded_senseis == ['foo', 'bar']


##############################################################################

# HELP COMMAND

##############################################################################

def test_should_request_manual_when_help_parameter_is_present():
    # TEST
    arguments = from_command("/random-sensei -h")
    
    # ASSERT 
    assert arguments.manual == True

def test_should_request_manual_when_help_parameter_is_present_in_full_syntax():
    # TEST
    arguments = from_command("/random-sensei --help")
    
    # ASSERT 
    assert arguments.manual == True


def test_should_not_request_manual_when_help_parameter_is_absent():
    # TEST
    arguments = from_command("/random-sensei -holo")
    
    # ASSERT 
    assert arguments.manual == False

##############################################################################

# LIMIT CASES

##############################################################################


def test_should_throw_an_exception_when_command_does_not_start_with_random_sensei():
    with pytest.raises(SenseiCommandException):
        from_command('coucou random-sensei')

# TODO tester avec un autre argument derrière