from flask_restx import Namespace, fields

class PhoneDto:
    """
    DTO Phone
    """
    api = Namespace("Phone", description="Endpoints API Agente Virtual")

    phone_remove = api.model('phone_remove', {
        'phone_id': fields.Integer(required=True, description="Id do telefone"),
    })

    phone_post = api.model('phone_post', {
        'phone_number': fields.String(required=True, description="Número de telefone"),
        'available': fields.Boolean(description="Disponível para discagem"),
    })

    phone = api.model('Phone', {
        'phone_id': fields.Integer(required=True, description="Id do telefone PHONE"),
        'phone_number': fields.String(required=True, description="Número de telefone"),
        'available': fields.Boolean(description="Disponível para discagem"),
    })

