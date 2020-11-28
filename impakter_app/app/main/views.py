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


@main.route('/add/<requested_item>',methods = ['GET','POST'])
def add_user(requested_item):
    item = requested_item

    if requested_item == 'user':
        form = UserForm()
        status = 'connection active'
        if form.validate_on_submit():
            new_record = User(username = form.username.data,name = form.first_name.data + ' ' + form.last_name.data)
            try:
                db.session.add(new_record)
                db.session.commit()
                added_record = User.query.filter_by(username=form.username.data).first()
                status = f'Successfully added {added_record.name} to database'
            except:
                status = "Unable to add the record to database. Please contact admin"

            form = UserForm()
            return render_template('add.html', status = status,form = form,item=item)

    if requested_item == 'source':
        form = SourceForm()
        status = 'connection active'
        if form.validate_on_submit():
            new_record = Source(name = form.name.data,type = form.type.data,rating = form.rating.data)
            try:
                db.session.add(new_record)
                db.session.commit()
                added_record = Source.query.filter_by(name=form.name.data).first()
                status = f'Successfully added {added_record.name} to database'
            except:
                status = "Unable to add the record to database. Please contact admin"

            form = SourceForm()
            return render_template('add.html', status = status,form = form,item = item)

    if requested_item == 'company':
        form = CompanyForm()
        status = 'connection active'
        if form.validate_on_submit():
            new_record = Company(name = form.name.data,
            address = form.address.data,company_url = form.url.data,revenue = form.revenue.data,
            financial_year = form.financial_year.data,country = form.country.data,
            stock_market = form.stock_market.data,ticker = form.ticker.data,
            company_desc = form.company_desc.data,company_desc_long= form.company_desc_long.data,
            rating = form.rating.data)
            try:
                db.session.add(new_record)
                db.session.commit()
                added_record = Company.query.filter_by(name=form.name.data).first()
                status = f'Successfully added {added_record.name} to database'
            except:
                status = "Unable to add the record to database. Please contact admin"

            form = CompanyForm()
            return render_template('add.html', status = status,form = form,item = item)     

    if requested_item == 'credential':
        form = CredentialForm()
        status = 'connection active'
        if form.validate_on_submit():
            new_record = Credential(name = form.name.data,type = form.type.data,rating = form.rating.data)
            try:
                db.session.add(new_record)
                db.session.commit()
                added_record = Credential.query.filter_by(name=form.name.data).first()
                status = f'Successfully added {added_record.name} to database'
            except:
                status = "Unable to add the record to database. Please contact admin"

            form = CredentialForm()
            return render_template('add.html', status = status,form = form,item = item) 

    return render_template('add.html',form = form,item = item)


@main.route('/add_company',methods = ['GET','POST'])
def add_company():
    form = CompanyForm()
    status = 'connection active'
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('add.html',form=form,name= name)

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

@main.route('/show/<requested_item>/<int:page>',methods = ['GET','POST'])
def show(requested_item,page):
    if requested_item == 'companies':
        table = Company.query.all()[page:page+10]
        item = requested_item
        return render_template('companies.html',table = table,item = item)

    if requested_item == 'users':
        table = User.query.all()[page:page+10]
        item = requested_item
        return render_template('users.html',table = table,item = item)

    if requested_item == 'sources':
        table = Source.query.all()[page:page+10]
        item = requested_item
        return render_template('sources.html',table = table,item = item)

    if requested_item == 'credentials':
        x= page
        table = Credential.query.all()[page:page+10]
        item = requested_item
        return render_template('credentials.html',table = table,item = item)
    
    return render_template('home.html',**kwargs)



@main.route('/users',methods = ['GET','POST'])
def users():
    userTable = User.query.all()[1:3]
    status = 'retrieved'
    return render_template('users.html',table = userTable, status = status)


@main.route('/sources',methods = ['GET','POST'])
def sources():
    sourceTable = Source.query.all()
    status = 'retrieved'
    return render_template('sources.html',table = sourceTable, status = status)


@main.route('/companies',methods = ['GET','POST'])
def companies():
    companyTable = Company.query.all()
    status = 'retrieved'
    return render_template('companies.html',table = companyTable, status = status)

@main.route('/credentials',methods = ['GET','POST'])
def credentials():
    credentialTable = Credential.query.all()
    status = 'retrieved'
    return render_template('credentials.html',table = credentialTable, status = status)

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


