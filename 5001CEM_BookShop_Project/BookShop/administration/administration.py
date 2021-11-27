#Core required Libraries for module execution
from flask import Flask, url_for, render_template, request, redirect, abort, make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re

administration = Blueprint('administration',__name__,
                          template_folder="templates",
                          static_folder="static")

@administration.route('/admin_dashboard', methods=['GET'])
def adminDashboard():
    dbConnection = sqlite.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    return render_template("administration.html",Products=rows)

@administration.route('/delete_record', methods=['POST','GET'])
def delete_record(ISBN):
    dbConnection = sqlite.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("DELETE FROM products WHERE ISBN13=?",(ISBN,))
    
    
    


        
