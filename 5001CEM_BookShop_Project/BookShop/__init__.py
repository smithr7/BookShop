#Tutorial: https://hackersandslackers.com/flask-blueprints/
from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)
    app.config['FLASK_ENV'] = 'development'
    app.config['SECRET_KEY'] = '625273'
    
    with app.app_context():
        from .loginCredentials.loginCredentials import loginCredentials
        
        app.register_blueprint(loginCredentials,url_prefix="/login")
        