#Core required Libraries for module execution
from flask import Flask, url_for, render_template, request, redirect, abort, make_response
#Module registration information
from flask import Blueprint
from flask import current_app as app
#Database libraries modules required
from markupsafe import escape
import sqlite3, os, re

#Administration blueprint extension script
administration = Blueprint('administration',__name__,
                          template_folder="templates",
                          static_folder="static")

#Base administration URL
@administration.route('/', methods=['GET','POST'])
def adminDashboard():
    dbConnection = sqlite3.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    return render_template("administration.html",Products=rows)

#Deleting record from current database
@administration.route('/delete_record/<string:ISBN>', methods=['POST','GET'])
def delete_record(ISBN):
    dbConnection = sqlite3.connect('./Database/bookProducts.db')
    cursor = dbConnection.cursor()
    cursor.execute("DELETE FROM products WHERE ISBN13=?",(ISBN,))
    dbConnection.commit()
    cursor.close()
    dbConnection.close()
    return redirect('/admin_dashboard')

#Add new record to current database
@administration.route('/add_new_book', methods=['GET','POST'])
def addNewBook():
     if request.method == 'POST':
        dbConnection = sqlite3.connect('./Database/bookProducts.db')
        cursor = dbConnection.cursor()
        
        bookAttr = ['ISBN13','Title','Author','genre','pubDate','type','tradePrice','retailPrice','quantity']
        bookFormInfo = []
            
        for index in bookAttr:
            bookFormInfo.append(request.form[index])
        
        cursor.execute("INSERT INTO products (ISBN13,book_description,author_name,genre,publication_date,book_type,trade_price,retail_price,book_quantity) VALUES (?,?,?,?,?,?,?,?,?)",(bookFormInfo[0],bookFormInfo[1],bookFormInfo[2],bookFormInfo[3],bookFormInfo[4],bookFormInfo[5],bookFormInfo[6],bookFormInfo[7],bookFormInfo[8]))
        
        dbConnection.commit()
        
        cursor.close()
        dbConnection.close()
        return redirect('/admin_dashboard')

    
    
    


        
