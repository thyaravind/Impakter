from flask import Flask, render_template,request, flash, redirect, url_for
import os.path
import json
from werkzeug.utils import secure_filename

from ..models import User,Credential,Company,Source
from .. import db
from . import main
from .forms import UserForm,CredentialForm,CompanyForm,SourceForm

kwargs = {}


@main.route('/',methods = ['GET','POST'])
def home():
    return render_template('home.html')


@main.route('/add_user',methods = ['GET','POST'])
def add_user():
    form = UserForm()
    status = 'connection active'
    if form.validate_on_submit():
        user = User(username = form.username.data,name = form.first_name.data + ' ' + form.last_name.data)
        db.session.add(user)
        db.session.commit()
        added_user = User.query.filter_by(username=form.username.data).first()
        status = f'{added_user.name} is added to db'
        return render_template('updated.html', status = status)
    return render_template('add.html',form = form)


@main.route('/add_company',methods = ['GET','POST'])
def add_company():
    name = None
    form = CompanyForm()
    status = 'connection active'
    if form.validate_on_submit():
        info = {}
        
        info = {
            'id': form.name.data+form.ticker.data,
            'company_name': form.name.data,
            'company_url': form.company_url.data,
            'address': form.address.data,
            'country': form.country.data,
            'stock_market':form.stock_market.data,
            'ticker': form.ticker.data,
            'revenue': form.revenue.data,
            'financial_year': form.financial_year.data,
            'desc': form.company_desc.data,
            'desc_long': form.company_desc_long.data,
            'sus': form.sustainability.data,
            'sus_long': form.sustainability_long.data,
            'critical_points': form.critical_points.data,
            'outlook':form.outlook.data,
            'notes':form.notes.data,
            'rating':form.rating.data
        }


        name = form.name.data
        form.name.data=''
    return render_template('add.html',form=form)

@main.route('/add_credential',methods = ['GET','POST'])
def add_credential():
    name = None
    form = CredentialForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('add.html',form=form)

@main.route('/add_source',methods = ['GET','POST'])
def add_source():
    name = None
    form = SourceForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('add.html',form=form)


@main.route('/users',methods = ['GET','POST'])
def users():
    userTable = User.query.all()
    status = 'retrieved'
    return render_template('users.html',table = userTable, status = status)




@main.route('/companies',methods = ['GET','POST'])
def companies():
    companyTable = Company.query.all()
    

    return render_template('companies.html',value = data,status = kwargs['status'])

@main.route('/credentials',methods = ['GET','POST'])
def companies():
    credentialTable = m.User.query.all()
    status = 'retrieved'
    return render_template('credentials.html',table = userTable, status = status)

@main.route('/research',methods = ['GET','POST'])
def research():
    return render_template('research.html')


@main.route('/upload_company',methods = ['GET','POST'])
def upload_company():
    if request.method == 'POST':

        info = {}
        info = {
            'id': request.form['company_name'][0:3]+request.form['ticker'],
            'company_name': request.form['company_name'],
            'company_url': request.form['company_url'],
            'address': request.form['address'],
            'country': request.form['country'],
            'stock_market':request.form['stock_market'],
            'ticker': request.form['ticker'],
            'revenue': request.form['company_revenue'],
            'financial_year': request.form['financial_year'],
            'desc': request.form['company_description'],
            'desc_long': request.form['company_description_long'],
            'sus': request.form['sustainability'],
            'sus_long': request.form['sustainability_long'],
            'critical_points': request.form['critical_points'],
            'outlook':request.form['outlook'],
            'notes':request.form['notes'],
            'rating':request.form['rating'],

        }
        kwargs = {}
        kwargs['company'] = info['company_name']

        return render_template('updated.html',**kwargs)

@main.route('/updated',methods = ['GET','POST'])
def updated():
    

    return render_template('updated.html',**kwargs)


