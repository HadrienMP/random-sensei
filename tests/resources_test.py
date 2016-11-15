import os

from flask import url_for
from mock import Mock

from application.services import *
from application.services import argument_extractor
from application.services.argument_extractor import SenseiCommandException


def test_integration_nominal_case(client):
    # SETUP
    request = build_request_with_command("/sensei")

    # TEST
    response = client.post(url_for('random_sensei'), data=request).json

    # ASSERT
    assert response['color'] != ''
    assert response['message'] != ''
    assert '@HadrienMensPellen Looks like you are going to have to be your own master...\n' in response['message']


def test_full_command_with_mocked_hip_chat(client, mocker):
    # SETUP
    mocker.patch('application.services.hipchat_client.get_room_members')
    hipchat_client.get_room_members = Mock(return_value=['foo', 'bar', 'qix', 'qux', 'qax', 'qex', 'HadrienMensPellen'])

    request = build_request_with_command("/sensei 4 --without foo bar")

    # TEST
    response = client.post(url_for('random_sensei'), data=request).json

    # ASSERT
    assert response['color'] != ''
    assert response['message'] != ''
    assert 'foo' not in response['message']
    assert 'bar' not in response['message']

    assert 'qix' in response['message']
    assert 'qux' in response['message']
    assert 'qax' in response['message']
    assert 'qex' in response['message']


def test_should_return_a_red_error_message_when_command_is_not_well_formed(client, mocker):
    # SETUP
    mocker.patch('application.services.argument_extractor.from_command')
    argument_extractor.from_command = Mock(side_effect=SenseiCommandException(""))

    request = build_request_with_command("not valid command")

    # TEST
    response = client.post(url_for('random_sensei'), data=request)

    # ASSERT
    assert response.json['color'] == "red"
    assert "talking to me" in response.json['message']


def build_request_with_command(command):
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(dir + '/request_template.json', 'r') as f:
        request = f.read()
    request %= command
    return request

