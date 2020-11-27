import os
from flask_sqlalchemy import SQLAlchemy
from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    name = db.Column(db.String(64))

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    company_url = db.Column(db.String(64))
    address = db.Column(db.String(64))
    country = db.Column(db.String(64))
    stock_market = db.Column(db.String(64))
    ticker = db.Column(db.String(64))
    revenue = db.Column(db.String(64))
    financial_year = db.Column(db.String(64))
    company_desc = db.Column(db.String(64))
    company_desc_long = db.Column(db.String(64))
    sustainability = db.Column(db.String(64))
    sustainability_long = db.Column(db.String(64))
    critical_points = db.Column(db.String(64))
    outlook = db.Column(db.String(64))
    notes = db.Column(db.String(64))
    rating = db.Column(db.String(64))


class Credential(db.Model):
    __tablename__ = 'credentials'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))

class Source(db.Model):
    __tablename__ = 'sources'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))


