from mock import Mock

from application.services.sensei_message_service import *


def test_should_return_the_number_of_senseis_asked_in_the_argument_string():
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=['1', '2', '3', '4'])
    number_of_senseis = 3

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == int(number_of_senseis)


def test_should_return_no_sensei_for_a_number_of_senseis_of_0():
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=['1', '2', '3', '4'])
    number_of_senseis = 0

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == 0


def test_should_return_no_sensei_for_a_negative_number_of_senseis():
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=['1', '2', '3', '4'])
    number_of_senseis = -1

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == 0


def test_should_return_no_sensei_when_the_room_is_empty():
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=[])
    number_of_senseis = 4

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == 0


def test_should_return_no_sensei_when_the_room_contains_only_the_requester():
    # SETUP
    requester = "Test"
    hipchat_client.get_room_members = Mock(return_value=[requester])
    number_of_senseis = 4

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test', requester=requester)

    # ASSERT
    # The only @ will be for the requester
    assert message.count('@') == 1


def test_should_return_all_as_sensei_when_more_senseis_are_requested_than_available():
    # SETUP
    hipchat_client.get_room_members = Mock(return_value=['1', '2', '3', '4'])
    number_of_senseis = 10

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == 1
    assert '@all' in message


def test_should_return_all_as_sensei_when_all_are_required():
    # SETUP
    senseis = ['1', '2', '3', '4']
    hipchat_client.get_room_members = Mock(return_value=senseis)
    number_of_senseis = len(senseis)

    # TEST
    message = random_senseis_message(number_of_senseis=number_of_senseis, room='test')

    # ASSERT
    assert message.count('@') == 1
    assert '@all' in message


def test_should_not_include_exluded_sensei():
    # SETUP
    senseis = ['1', '2', '3', '4']
    hipchat_client.get_room_members = Mock(return_value=senseis)

    # TEST
    message = random_senseis_message(room='test', number_of_senseis=2, excluded_senseis='1')

    # ASSERT
    assert '@1' not in message


def test_should_not_include_exluded_senseis():
    # SETUP
    senseis = ['1', '2', '3', '4', '5']
    hipchat_client.get_room_members = Mock(return_value=senseis)

    # TEST
    message = random_senseis_message(room='test', number_of_senseis=2, excluded_senseis=['1', '2'])

    # ASSERT
    assert '@1' not in message
    assert '@2' not in message


def test_should_not_exclude_nor_include_member_that_is_not_in_room():
    # SETUP
    senseis = ['2', '3', '4']
    hipchat_client.get_room_members = Mock(return_value=senseis)

    # TEST
    message = random_senseis_message(room='test', number_of_senseis=2, excluded_senseis='1')

    # ASSERT
    assert '@1' not in message


def test_should_not_return_all_as_master_when_a_member_was_excluded_from_the_senseis():
    # SETUP
    senseis = ['1', '2', '3']
    hipchat_client.get_room_members = Mock(return_value=senseis)

    # TEST
    message = random_senseis_message(room='test', number_of_senseis=2, excluded_senseis='1')

    # ASSERT
    assert '@1' not in message
    assert '@all' not in message


# TODO ajouter des tests pour les senseis exclus multiples