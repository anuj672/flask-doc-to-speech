from flask import Blueprint, request
import os

route_polly = Blueprint('route_polly', __name__)

@route_polly.route('/')
def home():
    return "Welcome!"