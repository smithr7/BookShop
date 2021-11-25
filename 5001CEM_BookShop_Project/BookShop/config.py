from os import environ
import redis

class Config:
    #Flask environment
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    
    #Flask session
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))
    
    LESS_BIN = '../../venv/lib/python3.6/site-packages/lesscpy/lessc'
    ASSETS_AUTO_BUILD = True
    DATABASE_URI = './BookShop/Database/'
    MAX_COOKIE_SIZE = '4093'
    