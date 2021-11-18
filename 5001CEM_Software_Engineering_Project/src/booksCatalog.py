from markupsafe import escape
from flask import Flask, session, url_for, render_template, request, redirect, abort, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from re import *
import sys,os

app = Flask(__name__, template_folder='../web/templates/')

@app.route('/books')
def loadBookProducts():
    path = './Database/bookProducts.db'
    con = sqlite3.connect(path)
    cur = con.cursor();
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    return render_template('bookCatalog.html',products=rows)

