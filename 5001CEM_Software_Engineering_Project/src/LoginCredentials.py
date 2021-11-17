from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import make_response
import sqlite3
import os
import re

app = Flask(__name__, template_folder='../web/templates/')
regularExpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Login action
#------------------------------------------------------------------------------------------------------------------------------------

#Login url extension
@app.route('/', methods=['GET','POST'])
#Login data request from HTML form
def login():
    if request.method == 'POST':
        #email address validation check
        if(re.fullmatch(regularExpression,requestform['username'])):
            return login_process(request.form['username'], request.form['password'])
        else:
            abort(403)
    else:
        return display_login()
    
#Display of login html webpage
def display_login():
    return render_template('LoginCredentials.html',page=url_for('login'))

#Validate login credentials against stored data
def login_process(username, password):
    #Database connection
    databaseConnection = sqlite3.connect('./Database/userCredentials.db')
    current = databaseConnection.cursor();
    #Query issued to database
    current.execute("SELECT count(*) FROM userCredentials WHERE email_address = ? AND password = ?;",(username,password))
    #Ensuring user/administrative record exists
    if(int(current.fetchone()[0]))>0:
        return render_template('LoginCredentials.html',page=url_for('login'))
    else:
        #Failure to locate re-loads form
        return render_template('LoginCredentials.html',page=url_for('login'))

#Register action
#----------------------------------------------------------------------------------------------------------------------------------------

#Registering data request from HTML form
@app.route('/register', methods=['GET','POST'])

def register():
    if request.method == 'POST':
        #email address validation check
        if(re.fullmatch(regularExpression,requestform['email'])):
            return registration_process(request.form['email'], request.form['password'], request.form['first_name'], request.form['second_name'], request.form['other_names'], request.form['DOB'])
        else:
            abort(403)
    else: 
        return display_registration_form();

#Requesting HTML template for user to enter registration data
def display_registration_form():
    return render_template('Register.html',page=url_for('register'))

#Database registration data input
def registration_process(email,password,fname,sname,oname,dob):
    #Database connection
    databaseConnection = sqlite3.connect('./Database/userCredentials.db')
    #Insert function arguments into database via insert query
    databaseConnection.execute("INSERT INTO userCredentials values(?,?,?,?,?,?);", (email,password,fname,sname,oname,dob))
    databaseConnection.commit
    #Close database connection
    databaseConnection.close()
    #Display blank registration form as success
    return display_registration_form()

    