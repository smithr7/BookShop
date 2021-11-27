
class Config:
    #Flask environment
    SECRET_KEY = '625273'
    FLASK_ENV = 'Development'
    TESTING = True
    DEBUG = True
    
    LESS_BIN = '../../venv/lib/python3.6/site-packages/lesscpy/lessc'
    ASSETS_AUTO_BUILD = True
    DATABASE_URI = './BookShop/Database/'
    MAX_COOKIE_SIZE = '4093'
    