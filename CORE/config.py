import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'adlkashfksghagh' #todo - get from environment variables -- replace with os.envron.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_SECRET_KEY="werrqwrtwrwewertrtewt"
    WTF_CSRF_ENABLED = False


    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, '../DB/data.sqlite') #todo add MySQL Url


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aravind:impakter@localhost/impakter_index' #todo add MySQL Url - test set

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://aravind:impakter@localhost/impakter_index' #todo add MySQL Url - Actual DB


config_option = {
    'development' : DevConfig,
    'testing' : TestConfig,
    'production' : ProductionConfig,
    'default' : DevConfig
}
