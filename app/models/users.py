import uuid
from sanic.response import text
from sanic import Blueprint
from app import db
from sqlalchemy import String, Date, Text, DateTime, Boolean, BigInteger
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Individuals(db.Model):
    __tablename__ = 'individuals'

    individual_id = Column(String(25), primary_key=True, default=str(uuid.uuid4().int)[:25])
    firstname = Column(String(40), nullable=True)
    lastname = Column(String(40), nullable=True)
    phone = Column(String(14), nullable=False, unique=True)
    dateofbirth = Column(Date, nullable=False, default='1900-01-01')
    address = Column(Text(), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    confirmed = Column(Boolean, default=False)
    indi_id = relationship('user_accounts', backref='individuals')
    img_id = relationship('image_accounts', backref='individuals')

    def __repr__(self):
        return '{}'.format(self.individual_id)

class UserAccount(db.Model):
    __tablename__ = 'user_accounts'

    user_account_id = Column(String(25), primary_key=True, default=str(uuid.uuid1().int)[:25])
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    individual_id = Column(String(25), ForeignKey('individuals.individual_id'))
    roleid = relationship('user_roles', backref='user_accounts')

    def __repr__(self):
        return '{}'.format(self.user_account_id)

class Images(db.Model):
    __tablename__ = 'images'

    image_id = Column(String(10), primary_key=True, default=str(uuid.uuid1().int)[:10])
    source_url = Column(Text(), nullable=False, default='https://cdn.pixabay.com/photo/2017/06/13/12/53/profile-2398782_960_720.png')
    status_upload = Column(String(10), nullable=False, default='200')
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '{}'.format(self.image_id)

class ImageAccounts(db.Model):
    __tablename__ = 'image_accounts'

    individual_id = Column(String(25), ForeignKey('individuals.individual_id'))
    image_id = Column(String(10), ForeignKey('images.image_id'))

class Roles(db.Model):
    __tablename__ = 'roles'

    role_id = Column(String(7), primary_key=True, default=str(uuid.uuid4().int)[:7])
    description = Column(String(25), nullable=False)

    def __repr__(self):
        return '{}'.format(self.role_id)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    role_id = Column(String(7), ForeignKey('roles.role_id'))
    user_account_id = Column(String(25), ForeignKey('user_accounts.user_account_id'))