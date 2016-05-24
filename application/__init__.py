# -*-  coding: utf-8-*-
from flask import Flask
import os

app = Flask(__name__)

config_object_path = os.getenv('RANDOM_SENSEI_CONFIG_OBJECT', 'config.default.Config')
app.config.from_object(config_object_path)

from application.resources import *
