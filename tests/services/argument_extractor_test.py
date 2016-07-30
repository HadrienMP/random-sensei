# -*- coding: utf-8 -*-
from mock import Mock

from application.services.argument_extractor import *


def test_should_return_number_of_senseis_when_present():
    # TEST
    arguments = from_command('/random-sensei  10      ')

    # ASSERT
    assert arguments.number_of_senseis == 10
    assert len(arguments.excluded_senseis) == 0


def test_should_extract_number_of_sensei_when_other_arguments_are_present_after():
    # TEST
    arguments = from_command('/random-sensei  8   test   ')

    # ASSERT
    assert arguments.number_of_senseis == 8
    assert len(arguments.excluded_senseis) == 0


def test_should_not_extract_number_of_sensei_when_other_arguments_are_present_before():
    # TEST
    arguments = from_command('/random-sensei test  140   ')

    # ASSERT
    assert arguments.number_of_senseis == 2
    assert len(arguments.excluded_senseis) == 0


def test_should_use_default_arguments_when_absent():
    # TEST
    arguments = from_command('/random-sensei')

    # ASSERT
    assert arguments.number_of_senseis == 2
    assert len(arguments.excluded_senseis) == 0


def test_should_extract_excluded_senseis():
    # TEST
    arguments = from_command('/random-sensei -foo -bar')

    # ASSERT
    assert arguments.excluded_senseis == ['foo', 'bar']


def test_should_extract_excluded_senseis_with_arobase():
    # TEST
    arguments = from_command('/random-sensei -@foo')

    # ASSERT
    assert arguments.excluded_senseis == ['foo']


def test_should_exclude_even_weird_names():
    # TEST
    arguments = from_command('/random-sensei -@[|{$ẑfgg')

    # ASSERT
    assert arguments.excluded_senseis == ['[|{$ẑfgg']
