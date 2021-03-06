#Core required Libraries for module execution
from flask import Flask, url_for, render_template, request, redirect, abort, make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re

registerCredentials = Blueprint('registerCredentials',__name__,
                                template_folder="templates",
                                static_folder="static")
#Validate email
regularExpression = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#Register action
#----------------------------------------------------------------------------------------------------------------------------------------

#Registering data request from HTML form
@registerCredentials.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #email address validation check
        if(re.fullmatch(regularExpression,request.form['email'])):
            return registration_process(request.form['email'], request.form['password'], request.form['first_name'], request.form['second_name'], request.form['other_names'], request.form['DOB'])
        else:
            abort(403)
    else: 
        print("Displaying register page")
        return display_registration_form();

#Requesting HTML template for user to enter registration data
def display_registration_form():
    return render_template('Register.html')

#Database registration data input
def registration_process(email,password,fname,sname,oname,dob):
    registered = False
    
    #Database connection
    databaseConnection = sqlite3.connect('./Database/userCredentials.db')
    cursor = databaseConnection.cursor();
    
    #Checking if record exists
    cursor.execute('SELECT count(*) FROM userCredentials WHERE email_address =?',email)
    if(int(current.fetchone()[0]) > 0):
        registered = True
        return render_template('Register.html',userExsists=registered)
    
    #Insert function arguments into database via insert query
    databaseConnection.execute("INSERT INTO userCredentials values(?,?,?,?,?,?);", (email,password,fname,sname,oname,dob))
    databaseConnection.commit
    #Close database connection
    databaseConnection.close()
    session['key'] = email
    #Display blank registration form as success
    return redirect('/index')
