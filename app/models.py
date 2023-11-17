from sqlalchemy_serializer import SerializerMixin

# from app import db
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import sqlalchemy as sa

#from app import db

#__basemodel = db.Model


# class User(UserMixin, __basemodel):
#     __tablename__ = 'users'
#     id = sa.Column(sa.Integer, primary_key=True)
#     username = sa.Column(sa.String(), index=True, unique=True)
#     password_hash = sa.Column(sa.String(128))
#
#     def __repr__(self):
#         return 'Пользователь {}'.format(self.username)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
class Servers(__basemodel):
    __tablename__ = 'servers'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(), index=True, unique=True)
    invite_code = sa.Column(sa.String)
    worlds = db.relationship('Worlds', backref='servers', lazy=True)


class Worlds(__basemodel):
    __tablename__ = 'worlds'
    id = sa.Column(sa.Integer, primary_key=True)
    path = sa.Column(sa.String)
    server_id = sa.Column(sa.String, db.ForeignKey('servers.id'))
