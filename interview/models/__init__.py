from datetime import datetime
from interview import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    verified_at = db.Column(db.DateTime, default=None)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=None)


class Cnab(db.Model):
    __tablename__ = 'cnabs'

    id = db.Column(db.Integer, primary_key=True)

    transaction_type = db.Column(db.Integer, nullable=False)
    occurrence_at = db.Column(db.DateTime, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    card = db.Column(db.String(12), nullable=False)
    store_owner = db.Column(db.String(14), nullable=False)
    store_name = db.Column(db.String(19), nullable=False)

    def __repr__(self):
        return '<{0} - {1}>'.format(self.__tablename__, self.id)
