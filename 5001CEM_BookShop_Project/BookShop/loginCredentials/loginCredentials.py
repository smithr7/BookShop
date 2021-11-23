#Core required Libraries for module execution
from flask import Flask, url_for, render_template, request, redirect, abort, make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re

loginCredentials = Blueprint('loginCredentials',__name__,
                             template_folder="templates",
                             static_folder='static')

regularExpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Login action
#------------------------------------------------------------------------------------------------------------------------------------

#Login url extension
@loginCredentials.route('/', methods=['GET','POST'])
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
    return render_template('LoginCredentials.html')

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

    