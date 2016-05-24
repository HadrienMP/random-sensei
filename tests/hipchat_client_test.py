from application import app
from application import hipchat_client


def test_should_return_room_members():
    # WHEN
    room_members = hipchat_client.room_members('2761495')
    
    # THEN
    assert room_members == ['HadrienMensPellen']


def test_should_return_an_empty_list_for_an_invalid_room_id():
    # WHEN
    room_members = hipchat_client.room_members('-1')
    
    # THEN
    assert room_members == list()