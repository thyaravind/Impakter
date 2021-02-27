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
    status = db.Column(db.String(64))
    industry = db.Column(db.String(64))
    company_url = db.Column(db.String(64))
    address = db.Column(db.Text)
    country = db.Column(db.String(64))
    stock_market = db.Column(db.String(64))
    ticker = db.Column(db.String(64))
    revenue = db.Column(db.Float)
    financial_year = db.Column(db.Integer)
    company_desc = db.Column(db.Text)
    company_desc_long = db.Column(db.Text)
    sustainability = db.Column(db.Text)
    sustainability_long = db.Column(db.Text)
    sdgs = db.Column(db.Text)
    sdg_desc = db.Column(db.Text)
    critical_points = db.Column(db.Text)
    outlook = db.Column(db.String(64))
    notes = db.Column(db.Text)
    rating = db.Column(db.String(64))


class Credential(db.Model):
    __tablename__ = 'credentials'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    is_essential = db.Column(db.Boolean,default = False)
    rating = db.Column(db.String(64))
    specificity = db.Column(db.String(64))
    industries = db.Column(db.Text)
    sdgs = db.Column(db.Text)
    credential_url = db.Column(db.String(64))
    validity = db.Column(db.String(64))
    data_availability_type = db.Column(db.String(64))
    directory_url = db.Column(db.String(64))
    update_frequency = db.Column(db.String(64))
    data_availability_notes = db.Column(db.Text)




class Source(db.Model):
    __tablename__ = 'sources'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    rating = db.Column(db.String(64))
    specificity = db.Column(db.String(64))
    industries = db.Column(db.Text)
    url = db.Column(db.String(64))
    update_frequency = db.Column(db.String(64))



class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String(64))
    specificity = db.Column(db.String(64))
    industries = db.Column(db.Text)
    url = db.Column(db.String(64))



