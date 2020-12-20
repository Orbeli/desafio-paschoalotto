from flask import request
from flask_restx import Resource
from phone.utils.phone_dto import PhoneDto
from phone.blueprints.main.service.phone_service import new_phone, list_phones, get_phone, remove_phone, remove_phone_list
from phone.models.phone_model import PhoneSchema

api = PhoneDto.api

_phone = PhoneDto.phone,

_phone_post = PhoneDto.phone_post,

_phone_remove = PhoneDto.phone_remove,


def validate_integer_query_string(param, default):
    try:
        param = int(param)
        return param
    except:
        pass

    return default


@api.route('/')
class PhoneController(Resource):
    def get(self):
        """Lista até 50 telefones por página."""
        blocked = validate_integer_query_string(
            param=request.args.get("blocked", ""), 
            default=""
        )
        page = validate_integer_query_string(
            param=request.args.get("page", 1), 
            default=1
        )
        per_page = validate_integer_query_string(
            param=request.args.get("per_page", 50), 
            default=50
        )
        phones = list_phones(page=page, per_page=per_page, blocked=blocked)

        if phones:
            return PhoneSchema(many=True).dump(phones)
        else:
            return {"message": "Telefone(s) não encontrado(s)!"}, 404

    @api.expect(_phone_post)
    def post(self):
        """Cadastra 1 ou N telefones."""
        phone_schema = PhoneSchema(many=True, exclude=['phone_id'])
        errors = phone_schema.validate(request.json)
        if errors:
            return {"message": "Erro ao realizar a requisicao", "validation": errors}, 400

        return new_phone(request.json)

    @api.expect(_phone_remove)
    def delete(self):
        """Remove 1 ou N telefones"""
        phone_schema = PhoneSchema(many=True, exclude=['phone_number', 'available'])
        errors = phone_schema.validate(request.json)
        if errors:
            return {"message": "Erro ao realizar a requisicao", "validation": errors}, 400

        return remove_phone_list(request.json)

@api.route("/<phone_id>")
class PhoneControllerOperations(Resource):
    def get(self, phone_id):
        """Retorna telefone pelo id"""
        phone = get_phone(phone_id)
        if phone:
            return PhoneSchema(many=False).dump(phone)
        
        return {"message": "Telefone não encontrado!"}, 404

    def delete(self, phone_id):
        """Remove telefone pelo id"""
        phone = remove_phone(phone_id)
        if phone:
            return None, 204
        else:
            return {"message": "Telefone não encontrado!"}, 404 
