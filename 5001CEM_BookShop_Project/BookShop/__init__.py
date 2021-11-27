#Tutorial: https://hackersandslackers.com/flask-blueprints/
import os, sys
from flask import Flask
from flask_session import Session
from flask_assets import Environment

sessionInstance = Session()

#Create BookShop Flask instance
def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()
    
    sessionInstance.init_app(app)
    assets.init_app(app)

    
    #Fetching Flask Blueprint templates to load into instance
    with app.app_context():
        from .loginCredentials.loginCredentials import loginCredentials
        from .registerCredentials.registerCredentials import registerCredentials
        #from .checkout.checkout import checkout
        from .indexScript.indexScript import indexScript
        from .bookInformation.bookInformation import bookInformation
        from .booksCatalog.booksCatalog import booksCatalog
        from .assets import compile_static_assets

        #Binding all Blueprint templates into the instance
        app.register_blueprint(loginCredentials,url_prefix="/")
        app.register_blueprint(registerCredentials)
        app.register_blueprint(indexScript)
        #app.register_blueprint(checkout)
        app.register_blueprint(bookInformation)
        app.register_blueprint(booksCatalog)

        #Binding all Blueprint associated static instances into instance
        compile_static_assets(assets)

        return app
    
