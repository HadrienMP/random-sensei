# -*-  coding: utf-8-*-
from flask import jsonify
from flask import json
from flask import request
from application import app
import re
from application import services


MESSAGE_COLOR = "yellow"


@app.route("/", methods=['POST'])
def random_sensei():
    request_data = json.loads(request.data)
    
    arguments_string = _extract_arguments(request_data)
    requester = _extract_requester(request_data)
    requesters_room = _extract_requesters_room(request_data)
    message = services.get_message(arguments_string, requester, requesters_room)
    
    if not message:
        message = 'Wait... What ? (boom)'
    
    return jsonify({
        "color": MESSAGE_COLOR,
        "message": message,
        "notify": False,
        "message_format": "text"
    })
        
        
def _extract_arguments(request_data):
    command = request_data['item']['message']['message']
    
    m = re.search(r'/[^ ]+\s(.*)', command)
    if m:
        arguments_string = m.group(1)
    else:
        arguments_string = ''
        
    return arguments_string
    
    
def _extract_requester(request_data):
    return request_data['item']['message']['from']['mention_name']
    
    
def _extract_requesters_room(request_data):
    return request_data['item']['room']['id']