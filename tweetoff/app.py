from flask import Flask

def create_app():
    """create and configure an instance of Flask"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "WELCOME TO THE TWEETOFF"

    return app
