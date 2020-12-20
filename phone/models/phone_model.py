from phone.ext.database import db
from phone.ext.marshmallow import marshmallow

class Phone(db.Model):
    __tablename__ = 'phone'
    __table_args__ = {'extend_existing': True}
    phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(15), nullable=False)
    available = db.Column(db.Boolean, default=True, nullable=False)


class PhoneSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Phone
        load_schema = True