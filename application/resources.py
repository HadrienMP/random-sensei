# -*-  coding: utf-8-*-
from flask import json
from flask import jsonify
from flask import request

from application import app
from application.services import *
from application.services import argument_extractor

import random

MESSAGE_COLORS = ["yellow", "blue", "green", "purple"]


@app.route("/", methods=['POST'])
def random_sensei():
    request_data = json.loads(request.data)

    requesters_room = _extract_requesters_room(request_data)
    arguments = _extract_arguments(request_data)
    requester = _extract_requester(request_data)
    message = build_message(requesters_room, arguments, requester)

    return jsonify({
        "color": random.choice(MESSAGE_COLORS),
        "message": message,
        "notify": False,
        "message_format": "text"
    })


def _extract_arguments(request_data):
    command = request_data['item']['message']['message']

    return argument_extractor.from_command(command)


def _extract_requester(request_data):
    return request_data['item']['message']['from']['mention_name']


def _extract_requesters_room(request_data):
    return request_data['item']['room']['id']
