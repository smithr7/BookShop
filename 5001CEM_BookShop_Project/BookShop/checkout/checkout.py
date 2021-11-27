from flask import Flask
from flask import Blueprint
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response

checkout = Blueprint('checkout',__name__,
                             template_foler='templates',
                             static_folder='static')

@CreditCardProcess.route('/checkout',methods=['GET','POST'])
def displayCreditCardProcess():
    if request.method == 'POST':
        
    return render_template('checkout.html')
