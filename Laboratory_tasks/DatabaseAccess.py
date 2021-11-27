from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
import sqlite3

app = Flask(__name__)

@app.route("/create")
def create():
    con = sqlite3.connect('databaseDirectory/mydatabase.db')
    con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, id INT)')
    con.close()
    return "<h1>Table created successfully</h1>"

@app.route("/add")
def add_student():
    con = sqlite3.connect('databaseDirectory/mydatabase.db')
    cur = con.cursor()
    cname = 'Faye'
    cid = 10000
    cur.execute("INSERT INTO students (name,id) VALUES (?,?);",(cname,cid))
    con.commit()
    con.close()
    return "<h1>added students</h1>"

@app.route("/")
def top():
    con = sqlite3.connect("mydatabase.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * from students")
    rows = cur.fetchall();
    return render_template("students.html",rows = rows)