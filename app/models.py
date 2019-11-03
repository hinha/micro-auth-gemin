from datetime import datetime
# from sqlalchemy import Column
from sqlalchemy import String, Date, Text, DateTime, Boolean
# from app import db

# individuals = db.Table(
#     'individuals', db,
    
#     db.Column('individuals_id', db.String(25), primary_key=True),
#     db.Column('firstname', db.String(40), nullable=True),
#     db.Column('lastname', db.String(40), nullable=True),
#     db.Column('lastname', db.String(40), nullable=True),
# )

# class Individuals(db.Model):
#     __tablename__ = 'individuals'

#     individuals_id = db.Column(String(25), primary_key=True)
#     firstname = db.Column(String(40), nullable=True)
#     lastname = db.Column(String(40), nullable=True)
#     phone = db.Column(String(14), nullable=False, unique=True)
#     dateofbirth = db.Column(Date, nullable=False, default='1900-01-01')
#     address = db.Column(Text(), nullable=False)
#     created_at = db.Column(DateTime, default=datetime.now)
#     confirmed = db.Column(Boolean, default=False)
