from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
from flask import Blueprint
from flask import current_app as app

checkout = Blueprint('checkout',__name__,
                    template_folder='templates',
                    static_folder='static')

@checkout.route('/checkout',methods=['GET','POST'])
def displayCreditCardProcess():
    if request.method == 'POST':
        Address = request.form['addressLine1'] + request.form['addressLine2'] + request.form['addressLine3'] + request.form['addressLine4'] 
    return None

