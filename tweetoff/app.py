from flask import Flask
from .models import DB

def create_app():
    """create and configure an instance of Flask"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return "WELCOME TO THE TWEETOFF"

    return app
