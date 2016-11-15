# -*-  coding: utf-8-*-
from flask import json
from flask import jsonify
from flask import request
from flask import render_template

from application import app
from application.services import *
from application.services import argument_extractor

import random

from application.services.argument_extractor import SenseiCommandException

MESSAGE_COLORS = ["yellow", "blue", "green", "purple"]

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/", methods=['POST'])
def random_sensei():

    (message, color) = __build_response(request)

    return jsonify({
        "color": color,
        "message": message,
        "notify": False,
        "message_format": "text"
    })
    
def __build_response(request):
    try:
        request_data = to_json(request);
        requesters_room = _extract_requesters_room(request_data)
        arguments = _extract_arguments(request_data)
        requester = _extract_requester(request_data)
    
        message = build_message(requesters_room, arguments, requester)
        color = random.choice(MESSAGE_COLORS)
    except SenseiCommandException:
        message = "Are you talking to me ?" # TODO add a help command
        color = "red"
        
    return message, color
    
def to_json(request):
    try:
        return json.loads(request.data)
    except ValueError:
        raise SenseiCommandException("The request does not contain json");

def _extract_arguments(request_data):
    command = request_data['item']['message']['message']

    return argument_extractor.from_command(command)


def _extract_requester(request_data):
    return request_data['item']['message']['from']['mention_name']


def _extract_requesters_room(request_data):
    return request_data['item']['room']['id']
