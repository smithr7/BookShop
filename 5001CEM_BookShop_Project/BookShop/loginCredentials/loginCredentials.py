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

loginCredentials = Blueprint('loginCredentials',__name__,
                             template_folder="templates",
                             static_folder="static")

regularExpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Login action
#------------------------------------------------------------------------------------------------------------------------------------

#Login url extension
@loginCredentials.route('/', methods=['GET','POST'])
#Login data request from HTML form
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(login_user(username,password)):
            userSession(request.form['username'])
            return render_template(url_for('/index'),)
        else: 
            loginStatus = 'Failed'
            return render_template('LoginCredentials.html',login=loginStatus)
        
        next = flask.request.args.get('next')
        if not is_safe_url(next):
            return flask.abort(400)
        
        return redirect(next or flask.url_for('/index'))
    return render_template('LoginCredentials.html',login=url_for('login'))
        
def login_user(username,password):
    username = re.sub('[;]','',username)
    print(username)
    password = re.sub('[;]','',password)
    print(password)
    if(databaseAccess(username,password) > 0):
        return True
    else:
        return False

def userSession(userId):
    session['username'] = userId
    return 0
    
def databaseAccess(username,password):
    print("Current directory: {0}".format(os.getcwd()))
    databaseConnection = sqlite3.connect('./Database/userCredentials.db')
    cursor = databaseConnection.cursor();
    cursor.execute('SELECT count(*) FROM userCredentials WHERE email_address =? AND password =?',(username,password))
    return int(cursor.fetchone()[0])

    