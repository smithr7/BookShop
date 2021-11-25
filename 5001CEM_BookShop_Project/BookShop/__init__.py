#Tutorial: https://hackersandslackers.com/flask-blueprints/
from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config['FLASK_ENV'] = 'development'
    app.config['SECRET_KEY'] = '625273'
    
    with app.app_context():
        from .loginCredentials.loginCredentials import loginCredentials
        from .registerCredentials.registerCredentials import registerCredentials
        from .indexScript.indexScript import indexScript
        from .bookInformation.bookInformation import bookInformation
        from .booksCatalog.booksCatalog import booksCatalog
        
        app.register_blueprint(loginCredentials,url_prefix="/login")
        app.register_blueprint(registerCredentials)
        app.register_blueprint(indexScript)
        app.register_blueprint(bookInformation)
        app.register_blueprint(booksCatalog)
        
        return app
        