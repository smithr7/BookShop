#Tutorial: https://hackersandslackers.com/flask-blueprints/
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
sessionInstance = Session()
assets = Environment()

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')
    
    assets = Environment()
    assets.init_app(app)
    login_manager.init_app(app)
    sessionInstance.init_app(app)
    
    with app.app_context():
        from .loginCredentials.loginCredentials import loginCredentials
        from .registerCredentials.registerCredentials import registerCredentials
        from .indexScript.indexScript import indexScript
        from .bookInformation.bookInformation import bookInformation
        from .booksCatalog.booksCatalog import booksCatalog
        from .assets import compile_static_assets
    
        app.register_blueprint(loginCredentials,url_prefix="/login")
        app.register_blueprint(registerCredentials)
        app.register_blueprint(indexScript)
        app.register_blueprint(bookInformation)
        app.register_blueprint(booksCatalog)
        
        compile_static_assets(assets)
        
        return app
        