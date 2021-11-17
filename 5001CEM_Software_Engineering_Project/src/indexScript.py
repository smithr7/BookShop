from markupsafe import escape
from flask import Flask, session, url_for, render_template, request, redirect, abort, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
import re
import sys

app = Flask(__name__, template_folder='../web/templates/')
app.secret_key = "625273"


@app.route('/add', methods=['POST'])
def product_addition_to_cart():
    cursor = None
    try:
        quantity = int(request.form['quantity'])
        code = request.form['isbn']
        
        if code and (request.method == 'POST'):
            con = sqlite3.connect('./Database/bookProducts.db')
            cur = con.cursor();
            cur.execute("SELECT * FROM products WHERE ISBN13=?", [code])
            row = cur.fetchone()
            itemArray = {row[0] : {'ISBN13': row[0],'Author': row[1],'publication_date' : row[2],'book_description': row[3],'front_cover':row[4],'total_price': quantity * row[6],'price': row[6],'quantity': quantity}}
            
            overall_total_price = 0
            overall_total_quantity = 0
            
            session.modified = True
            
            if 'cart_item' in session:
                if row[0] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row[0] == key:
                            session['cart_item'][key]['quantity'] = quantity
                            previous_quantity = session['cart_item'][key]['quantity']
                            total_quantity = previous_quantity + quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row[7]
                else:
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)
                    print(session['cart_item'][key]['book_description'])                
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    overall_total_quantity = overall_total_quantity + individual_quantity
                    overall_total_price = overall_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                overall_total_quantity = overall_total_quantity + quantity
                overall_total_price = overall_total_price + quantity + row[7]
            
            session['overall_total_quantity'] = overall_total_quantity
            session['overall_total_price'] = overall_total_price
            
            return redirect(url_for('.loadHomeScreen'))
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e,exc_type, fname, exc_tb.tb_lineno)
    finally:
        cur.close()
        con.close()

@app.route('/index')
def loadHomeScreen():
    try:
        path = './Database/bookProducts.db'
        con = sqlite3.connect(path)
        cur = con.cursor();
        print(cur)
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        return render_template('index.html',products=rows)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        con.close()

@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('.products'))
    except Exception as e:
        print(e)
        
@app.route('/delete/<string:code>')
def delete_product(code):
    try:
        overall_total_price = 0
        overall_total_quantity = 0
        session.modified = True
        
        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0],None)
                if 'cart_item' in session:
                    for key, value in session:
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        overall_total_quantity = overall_total_quantity + individual_quantity
                        overall_total_price = overall_total_price + individual_price
                break
        if overall_total_quantity == 0:
            session.clear()
        else: 
            session['overall_total_quantity'] = overall_total_quantity
            session['overall_total_price'] = overall_total_price
        return redirect(url_for('.loadHomeScreen'))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e,exc_type, fname, exc_tb.tb_lineno)

def array_merge(first_array, second_array):
    if isinstance(first_array,list) and isinstance(second_array,list):
        return first_array + second_array
    if isinstance(first_array,dict) and isinstance(second_array,dict):
        return dict(list(first_array.items())+list(second_array.items()))
    if isinstance(first_array,set) and isinstance(second_array,set):
        return first_array.union(second_array)