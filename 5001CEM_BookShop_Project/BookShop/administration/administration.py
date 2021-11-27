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

@app.route('/delete_record', methods=['POST','GET'])
def delete_record(ISBN):
    dbConnection = sqlite.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("DELETE FROM products WHERE ISBN13=?",(ISBN,))

@app.route('/edit_item/<string:ISBN>', methods=['POST','GET'])
def edit(ISBN):
    dbConnection = sqlite.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    newQuantity = request.form['quantity']
    cursor.execute("UPDATE products SET quantity =? WHERE ISBN13 =?",(newQuantity,ISBN))
    return render_template("administration.html")
# <!--{% assets "indexScript_style_bundle" %}
#         <link 
#          rel="stylesheet" 
#          href="{{ ASSET_URL }}"
#          type="text/css"
#         />
#         {% endassets %}-->
    
    
    


        
