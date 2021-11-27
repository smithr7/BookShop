#Managing Session Data with Flask-Session & Redis, (2021), Todd, https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/
from os import environ, path
#from dotenv import load_dotenv

#primaryDir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir,'.env'))
import redis


class Config:
    #Flask environment
    SECRET_KEY = '625273'
    FLASK_APP = 'BookShop'
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    
    #Session initialisation
    SESSION_TYPE = 'filesystem'
    SESSION_PERMENANT = True
    PERMENANT_SESSION_LIFETIME = 60000
    
    LESS_BIN = '../../venv/lib/python3.6/site-packages/lesscpy/lessc'
    ASSETS_AUTO_BUILD = True
    
    