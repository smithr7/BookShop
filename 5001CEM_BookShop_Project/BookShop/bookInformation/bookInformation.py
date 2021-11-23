from markupsafe import escape
from flask import Flask, session, url_for, render_template, request, redirect, abort, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from re import *
import sys,os

#Flask object instantiation of class with webpage directory path specified
app = Flask(__name__, template_folder='../web/templates/')
app.secret_key = "625273"

@app.route('/bookDescription/<string:isbn>', methods=['POST'])
def bookDescription(isbn):
    con = sqlite3.connect('./Database/bookProducts.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE ISBN13=?",isbn)
    record = cur.fetchone()
    return render_template('bookPreview.html',product=isbn)