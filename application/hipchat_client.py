from application import app
import requests

def room_members():
    r = requests.get('http://darty-de.hipchat.com/v2/room/2761718/member?auth_token=' + app.config['HIPCHAT_TOKEN'])
    
    
    if r.status_code is 200:
        return [member['mention_name'] for member in r.json()['items']]
    else:
        print(app.config['HIPCHAT_TOKEN'])
        print(r.status_code)
        print(r.text)
        return []