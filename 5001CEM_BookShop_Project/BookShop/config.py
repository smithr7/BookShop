#Managing Session Data with Flask-Session & Redis, (2021), Todd, https://hackersandslackers.com/managing-user-session-variables-with-flask-sessions-and-redis/
class Config:
    #Flask environment
    SECRET_KEY = '625273'
    FLASK_APP = 'BookShop'
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
    
    #Session initialisation
    SESSION_TYPE = 'filesystem' #Requires local file system as no administrative privileges given
    SESSION_PERMENANT = True
    PERMENANT_SESSION_LIFETIME = 86400
    
    LESS_BIN = '../../venv/lib/python3.6/site-packages/lesscpy/lessc'
    ASSETS_AUTO_BUILD = True
    
    