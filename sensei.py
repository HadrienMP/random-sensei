# -*-  coding: utf-8-*-
from application import app
import os

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '8080')))