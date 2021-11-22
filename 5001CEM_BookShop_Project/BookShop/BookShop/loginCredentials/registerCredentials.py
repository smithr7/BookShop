from flask import Flask, url_for, render_template, request, redirect, abort, make_response
from flask import Blueprint
from markupsafe import escape
import sqlite3, os, re


registerCredentials = Blueprint('registerCredentials',__name__,
                             template_folder="templates",
                             static_folder='static')

#Register action
#----------------------------------------------------------------------------------------------------------------------------------------

#Registering data request from HTML form
@loginCredentials.route('/register', methods=['GET','POST'])

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
