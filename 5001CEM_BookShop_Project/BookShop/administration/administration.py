#Core required Libraries for module execution
from flask import Flask, url_for, render_template, request, redirect, abort, make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route('/admin_dashboard', methods=['GET','POST'])
def adminDashboard():
    dbConnection = sqlite3.connect('../Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    return render_template("administration.html",Products=rows)

#Deleting record from current database
@app.route('/delete_record/<string:ISBN>', methods=['POST','GET'])
def delete_record(ISBN):
    dbConnection = sqlite3.connect('../Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("DELETE FROM products WHERE ISBN13=?",(ISBN,))
    dbConnection.commit()
    cursor.close()
    dbConnection.close()
    return redirect('/admin_dashboard')

# @app.route('/add_new_book/', methods=['GET','POST'])
# def addNewBook():
#     if request.method == 'POST':
        
#     return redirect('/admin_dashboard')

# <!--{% assets "indexScript_style_bundle" %}
#         <link 
#          rel="stylesheet" 
#          href="{{ ASSET_URL }}"
#          type="text/css"
#         />
#         {% endassets %}-->
    
    
    


        
