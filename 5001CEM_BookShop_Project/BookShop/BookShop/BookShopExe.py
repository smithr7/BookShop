from flask import Flask
from loginCredentials import login, display_login, loginProcess, register, display_registration_form, registration_process
from indexScript import product_addition_to_cart, loadHomeScreen, empty_cart, delete_product, array_merge

app = Flask(__name__)
app.register_blueprint(loginCredentials)
app.register_blueprint(indexScript)
