import os
from importlib import import_module

file_path = os.path.abspath(os.getcwd())+"\database.db"

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

def load_extensions(app, extensions):
    for extension in extensions:
        module, factory = extension.split(':')
        ext = import_module(module)
        getattr(ext, factory)(app)
