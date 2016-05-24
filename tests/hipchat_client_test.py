from application import app
from application import hipchat_client

def test_should_return_room_members():
    print app.config['HIPCHAT_TOKEN']
    
    # WHEN
    room_members = hipchat_client.room_members()
    
    # THEN
    assert room_members == ['HadrienMensPellen']