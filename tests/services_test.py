from application.services import *
from mock import Mock
from application import hipchat_client

def test_should_return_3_senseis_for_an_argument_string_of_3():
    # Mock
    hipchat_client.room_members = Mock(return_value=['1', '2', '3', '4'])
    
    # WHEN
    message = get_message('3', room='test')
    
    # THEN
    assert message.count('@') == 3