from flask import Flask
from app.routes import route_polly

def create_app():
    app = Flask(__name__)
    app.register_blueprint(route_polly)
    return app
