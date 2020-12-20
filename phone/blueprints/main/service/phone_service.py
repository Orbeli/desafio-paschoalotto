from phone.models.phone_model import Phone
from phone.ext.database import db

def get_phone(phone_id):
    return Phone.query.get(phone_id)

def list_phones(blocked, page, per_page):
    #limito os itens a serem exibidos em no máximo 50 por página
    if per_page > 50:
        per_page = 50
    # Verifico se e necessario filtrar os resultados por telefones validos/invalidos
    if blocked == 1 or blocked == 0:
        return Phone.query.filter_by(available=blocked).paginate(page, per_page).items

    return Phone.query.paginate(page, per_page).items

def new_phone(phones):
    for phone in phones:
        new_phone = Phone()
        new_phone.phone_number = phone['phone_number'].strip()
        new_phone.available = phone['available']
        db.session.add(new_phone)
        db.session.commit()

    return {"message": "Telefone(s) inserido(s) com sucesso!"}, 201

def remove_phone_list(phone_ids):
    for phone_id in phone_ids:
        phone = Phone.query.get(phone_id)
        if phone:
            db.session.delete(phone)
            db.session.commit()

    return None, 204

def remove_phone(phone_id):
    phone = Phone.query.get(phone_id)
    if phone:
        db.session.delete(phone)
        db.session.commit()

    return phone