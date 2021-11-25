from flask import Flask
from flask import session
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from re import *
import sys,os

# bookInformation = Blueprint("bookInformation",__name__,
#                             template_folder='templates')
# bookInformation.secret_key = "625273"

#Testing purposes

app = Flask(__name__)

@app.route('/bookDescription', methods=['POST','GET'])
def bookDescription():
    isbn = "9780330520331"
    con = sqlite3.connect('../Database/bookProducts.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE ISBN13=?",(isbn,))
    record = cur.fetchone()
    return render_template('bookPreview.html',Product=record)

# @bookInformation.route('/bookDescription/<string:ISBN>', methods=['POST','GET'])
# def bookDescription(ISBN):
#     con = sqlite3.connect('../Database/bookProducts.db')
#     cur = con.cursor()
#     cur.execute("SELECT * FROM products WHERE ISBN13=?",(ISBN,))
#     record = cur.fetchone()
#     return render_template('bookPreview.html',product=record)