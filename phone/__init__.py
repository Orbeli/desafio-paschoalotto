from flask import Flask
from phone.ext import settings

def create_app():
    app = Flask(__name__)
    settings.init_app(app)

    settings.load_extensions(app, [
        'phone.ext.database:init_app',
        'phone.ext.marshmallow:init_app',
        'phone.blueprints.main:init_app'
    ])

    return app