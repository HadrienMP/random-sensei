import os

from flask import url_for
from application.services import hipchat_client
from mock import Mock


DIR = os.path.dirname(os.path.realpath(__file__))


def test_integration_nominal_case(client):
    # SETUP
    with open(DIR + '/example_request.json', 'r') as f:
        request = f.read()

    # TEST
    response = client.post(url_for('random_sensei'), data=request).json

    # ASSERT
    assert response['color'] != ''
    assert response['message'] != ''
    assert '@HadrienMensPellen Looks like you are going to have to be your own master...\n' in response['message']


def test_integration_nominal_case(client):
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=['foo', 'bar', 'qix', 'qux', 'qax', 'qex', 'HadrienMensPellen'])

    with open(DIR + '/full_request.json', 'r') as f:
        request = f.read()

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
