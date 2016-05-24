class Config():
    DEBUG = False
    HIPCHAT_TOKEN = 'room token'
    HIPCHAT_BASE_URL = 'http://darty-de.hipchat.com'
    HIPCHAT_ROOM_URL_FORMAT = HIPCHAT_BASE_URL + '/v2/room/{room}/member'
    
    
class DebugConfig(Config):
    DEBUG = True
    