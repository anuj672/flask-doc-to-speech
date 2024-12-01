from flask import Blueprint, request
import os

route_polly = Blueprint('route_polly', __name__)

@route_polly.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files.get('file')
        return "got it"   
    return "Welcome!"