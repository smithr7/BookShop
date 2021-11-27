#Core required Libraries for module execution
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from flask import session
from flask import make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re
#Authorisation imports
from flask_login import current_user, logout_user, login_required

loginCredentials = Blueprint('loginCredentials',__name__,
                             template_folder="templates",
                             static_folder="static")
regularExpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Login action
#------------------------------------------------------------------------------------------------------------------------------------

#Authentication process to index
@loginCredentials.route('/authenticated', methods=['GET'])
def loadMainPage():
    return redirect('/index')

#Login url extension
@loginCredentials.route('/', methods=['GET','POST'])
#Login data request from HTML form
def login():
    #Specify if POST method has been sent
    if request.method == 'POST':
        #Requesting form data to be stored
        username = request.form['username']
        password = request.form['password']
        loginStatus = ''
        #Securing email and password 
        if(login_user(username,password)):
            session['key'] = username
            #Redirection --Security flaw--
            return redirect('/authenticated')
        else: 
            #Login failed response 
            loginStatus = 'Failed'
            #Issue warning alert to user
            return render_template('LoginCredentials.html',login=loginStatus)
    #Return html and listen for form submission
    return render_template('LoginCredentials.html',login=url_for('.login'))

#Email and password security
def login_user(username,password):
    username = re.sub('[;]','',username)
    password = re.sub('[;]','',password)
    #Boolean return if record found
    if(databaseAccess(username,password) > 0):
        return True
        databaseConnection.close()
        cursor.close()
    else:
        return False
    
#Accessing database
def databaseAccess(username,password):
    print("Current directory: {0}".format(os.getcwd()))
    databaseConnection = sqlite3.connect('./Database/userCredentials.db')
    cursor = databaseConnection.cursor();
    cursor.execute('SELECT count(*) FROM userCredentials WHERE email_address =? AND password =?',(username,password))
    return int(cursor.fetchone()[0])

    