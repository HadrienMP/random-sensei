class Config():
    DEBUG = False
    HIPCHAT_TOKEN = 'room token'
    HIPCHAT_BASE_URL = 'https://api.hipchat.com'
    HIPCHAT_ROOM_URL_FORMAT = HIPCHAT_BASE_URL + '/v2/room/{room}/participant'
    MANUAL = '''Here are a few examples of how to use random-sensei : 
* Classic call with 2 senseis at random in the room /random-sensei
* n number of senseis : /random-sensei n
* Exclude people from the room (bad senseis) : /random-sensei -w @BadSensei @EvilSensei @NaziSensei
* A full example : /random-sensei 1 -w @BadSensei @EvilSensei @NaziSensei

Options:
* Number of senseis : -n or --number-of-senseis followed by a number
* Exclude sensei(s) : -w or --without followed by a list of people in the room
* Help : -h or --help'''
    
    
class DebugConfig(Config):
    DEBUG = True
    