from application.services import hipchat_client


def test_should_return_room_members(config):
    members = hipchat_client.get_room_members("2761495")
    assert members == ['HadrienMensPellen']


def test_should_return_empty_list_for_an_invalid_room_number(config):
    members = hipchat_client.get_room_members("-1")
    assert members == []
