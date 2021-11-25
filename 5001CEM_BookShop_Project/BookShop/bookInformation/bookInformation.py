from flask import Flask
from flask import session
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from re import *
import sys,os

app = Flask(__name__, template_folder='templates')
app.secret_key = "625273"

@app.route('/bookDescription', methods=['POST','GET'])
def bookDescription():
    isbn = "9780330520331"
    con = sqlite3.connect('../Database/bookProducts.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE ISBN13=?",(isbn,))
    record = cur.fetchone()
    return render_template('bookPreview.html',product=isbn)