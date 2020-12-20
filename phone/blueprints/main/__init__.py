from flask import Blueprint
from flask_restx import Api
from phone.blueprints.main.controllers.phone_controller import api as phone_ns

bp = Blueprint('api', __name__)

api = Api(
    bp,
    title="Api Agente Virtual",
    version="1.0.0",
    description="API Rest em Python utilizando Flask para a verificação se um ou mais telefones podem ou não ter acionamentos.",
    doc="/docs"
)

api.add_namespace(phone_ns, path="/phones")

def init_app(app):
    app.register_blueprint(bp, url_prefix='/api')