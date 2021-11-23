#Tutorial: https://hackersandslackers.com/flask-blueprints/
from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config['FLASK_ENV'] = 'development'
    app.config['SECRET_KEY'] = '625273'
    
    with app.app_context():
        from .loginCredentials import loginCredentials
        from .loginCredentials import registerCredentials
        from .indexScript import indexScript
        from .booksCatalog import bookCatalog
        
        app.register_blueprint(loginCredentials.loginCredentials,url_prefix="/login")
        app.register_blueprint(loginCredentials.registerCredentials)
        app.register_blueprint(indexScript.indexScript,url_prefix="/index")
        app.register_blueprint(booksCatalog.booksCatalog)
        