from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

def init_app(app):
    marshmallow.init_app(app)