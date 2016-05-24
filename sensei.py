# -*-  coding: utf-8-*-
from flask import Flask
from flask import jsonify
from flask import json
from flask import request
import re
import os
import services

app = Flask(__name__)


MESSAGE_COLOR = "yellow"


@app.route("/", methods=['POST'])
def random_sensei():
    request_data = json.loads(request.data)
    
    if _is_valid(request_data):
        arguments_string = _extract_arguments(request_data)
        requester = _extract_requester(request_data)
        message = services.get_message(arguments_string, requester)
    
    if not message:
        message = 'Wait... What ? (boom)'
    
    return jsonify({
        "color": MESSAGE_COLOR,
        "message": message,
        "notify": False,
        "message_format": "text"
    })
    
    
def _is_valid(request_data):
    return 'item' in request_data \
        and 'message' in request_data['item'] \
        and 'message' in request_data['item']['message'] \
        and 'from' in request_data['item']['message'] \
        and 'mention_name' in request_data['item']['message']['from']
        
        
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

if __name__ == "__main__":
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '8080')))