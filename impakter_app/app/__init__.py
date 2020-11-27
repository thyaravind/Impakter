from config import DevConfig

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os
basedir = os.path.abspath(os.path.dirname(__file__))


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()



def create_app():

    #initializing Flask app and config
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')
    app.config.from_object(DevConfig)


    #initializing extentions
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #attaching blueprints todo -- shorten by using importlib's import_module
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .news import news as news_blueprint


    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(news_blueprint)



    return app

