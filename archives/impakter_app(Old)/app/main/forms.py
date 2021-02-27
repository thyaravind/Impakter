from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FieldList, TextAreaField, RadioField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, AnyOf, InputRequired, URL

class CredentialForm(FlaskForm):
    name = StringField('Name of the certificate',validators=[InputRequired()])
    credential_type = SelectField('Select Type',choices=['Certificate','Ecolabel','Index'],validate_choice=True,default='Certificate')
    is_essential = BooleanField('Is Essential?')
    rating = SelectField('Level of Credibility',choices=['P-1','P-2','P-3','P-4'],validate_choice=True,default='P-1')

    specificity = RadioField('Specificity',choices=['Specific','Generic'],validate_choice=True,default='Generic')
    source_url = StringField('Source website URL',validators=[InputRequired(),URL()])

    submit = SubmitField('Submit')



class SourceForm(FlaskForm):
    name = StringField('Name of the source',validators=[InputRequired()])
    type = SelectField('Select Type',choices=['Research Report','News Publication','Other'],validate_choice=True,default='Certificate')
    rating = SelectField('Level of Credibility',choices=['FirstHand','Tier-1','Tier-2','Tier-3','Tier-4'],validate_choice=True,default='Tier-1')
    update_frequency = SelectField('Period of release',choices=['Real-time', 'Daily', 'Weekly', 'Monthly', 'Annual', 'Occasional'],validate_choice=True,default='Real-time')
    specificity = RadioField('Specificity',choices=['Specific','Generic'],validate_choice=True,default='Generic')
    url = StringField('Source website URL',validators=[InputRequired(),URL()])
    #todo industries multiselect





    submit = SubmitField('Submit')


class CompanyForm(FlaskForm):
    name = StringField('Name of the Company',validators=[InputRequired()])
    industry = SelectField('Select Industry',choices=['A','B'],validate_choice=True,default='A')
    status = SelectField('Mark Status',choices=['To double check','To triple check'],validate_choice=True)
    address = StringField('Address of the Company',validators=[InputRequired()])
    url = StringField('Company website URL',validators=[InputRequired(),URL()])
    revenue = StringField('Revenue in USD',validators=[InputRequired()])
    financial_year = SelectField('Financial Year',choices=[2019,2018,2017],validate_choice=True,default=2019)
    country = SelectField('Select Country',choices=['United States','United Kingdom'],validate_choice=True,default='United States')
    stock_market = SelectField('Select Stock Market',choices=['NASDAQ','NYSE'],validate_choice=True,default='NASDAQ')
    ticker = StringField("Company's stock ticker",validators=[InputRequired()],description = 'description',id=None,widget=None)

    company_desc = TextAreaField("Company's description",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)
    company_desc_long = TextAreaField("Company's description - Long ",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)

    #crendentials = SelectMultipleField('Select all Certificates and Indices',choices=['B Corp','USDA Organic'],default=None)
    awards = TextAreaField("Company's Awards",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)


    sustainability = TextAreaField("Company's Sustainability",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)
    sustainability_long = TextAreaField("Company's Sustainability Long",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)
    #sdgs = SelectMultipleField('Select SDGs',choices=['SDG 1','SDG 2'])
    critical_points = TextAreaField("Critical Points",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)
    notes = TextAreaField("Analyst's Notes",default = '', validators=[InputRequired()],description = 'description',id=None,widget=None)
    outlook = RadioField(label = "Outlook",default = 'Positive', choices=['Positive','Neutral','Negative'], validators=[InputRequired()],description = 'description',id=None,widget=None)
    rating = RadioField(label = "Rating",default = 'C', choices=['A - Extraordinary','B','C','D','E - fail'], validators=[InputRequired()],description = 'description',id=None,widget=None)
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    username = StringField('Create a username',validators=[InputRequired()])
    first_name = StringField('Enter your first Name',validators=[InputRequired()])
    last_name = StringField('Enter your first Name',validators=[InputRequired()])
    submit = SubmitField('Submit')
