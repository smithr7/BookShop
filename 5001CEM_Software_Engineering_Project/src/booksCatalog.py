from markupsafe import escape
from flask import Flask, session, url_for, render_template, request, redirect, abort, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from re import *
import sys, os, math

app = Flask(__name__, template_folder='../web/templates/')
app.secret_key = "625273"

@app.route('/add', methods=['POST'])
def product_addition_to_cart():
    cursor = None
    try:
        #Call-outs to forms of identifies of web elements quantity and isbn
        quantity = int(request.form['quantity'])
        code = request.form['isbn']
        
        #Conditional statement: request for POST issued and PK variable not empty
        if code and (request.method == 'POST'):
            #Database call-out
            con = sqlite3.connect('./Database/bookProducts.db')
            cur = con.cursor();
            #Issue request for all product items matching requested ISBN13
            cur.execute("SELECT * FROM products WHERE ISBN13=?", [code])
            row = cur.fetchone()
            #Dict instantiated with subcript values instantiating positioning
            itemArray = {row[0] : {'ISBN13': row[0],'Author': row[1],'publication_date' : row[2],'book_description': row[3],'front_cover':row[4],'total_price': quantity * row[6],'price': row[6],'quantity': quantity}}
            
            #Overall pricing and quantity
            overall_total_price = 0
            overall_total_quantity = 0
            
            session.modified = True
            
            #Check for session
            if 'cart_item' in session:
                #Conditional statement ensuring IBSN13 in current web session
                if row[0] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row[0] == key:
                            session['cart_item'][key]['quantity'] = quantity
                            previous_quantity = session['cart_item'][key]['quantity']
                            total_quantity = previous_quantity + quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row[7]

                else:
                #Failure/False condition issuing merger of database dict instantiation with web current session
                    session['cart_item'] = array_merge(session['cart_item'], itemArray) 
                #Totalling quantity for all products in web session basket
                for key, value in session['cart_item'].items():
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    overall_total_quantity = overall_total_quantity + individual_quantity
                    overall_total_price = overall_total_price + individual_price
            else:
                #Direct assignment to session web session
                session['cart_item'] = itemArray
                overall_total_quantity = overall_total_quantity + quantity
                overall_total_price = overall_total_price + quantity + row[7]
            
            session['overall_total_quantity'] = overall_total_quantity
            session['overall_total_price'] = overall_total_price
            
            #Redirection to home screen once completed
            return redirect(url_for('.loadBookProducts'))
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        # Exception handler pinpointing location of error raised
        # Extract source: https://www.codegrepper.com/code-examples/python/python+get+line+number+of+error
        # Website url: https://www.codegrepper.com/
        # Author: Confused Cottonmouth
        # Access date: 11/2021
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e,exc_type, fname, exc_tb.tb_lineno)
    finally:
        #Closing of database connection
        cur.close()
        con.close()

@app.route('/books')
def loadBookProducts():
    path = './Database/bookProducts.db'
    con = sqlite3.connect(path)
    cur = con.cursor();
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    productRows = len(rows) / 4
    if (len(rows) % 4) == 0:
        return render_template('bookCatalog.html',products=rows,gridRows=productRows)
    else:
        productRows = round(productRows)
        return render_template('bookCatalog.html',products=rows,gridRows=productRows)

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
		all_total_price = 0
		all_total_quantity = 0
		session.modified = True
		
		for item in session['cart_item'].items():
			if item[0] == code:				
				session['cart_item'].pop(item[0], None)
				if 'cart_item' in session:
					for key, value in session['cart_item'].items():
						individual_quantity = int(session['cart_item'][key]['quantity'])
						individual_price = float(session['cart_item'][key]['total_price'])
						all_total_quantity = all_total_quantity + individual_quantity
						all_total_price = all_total_price + individual_price
				break
		
		if all_total_quantity == 0:
			session.clear()
		else:
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price
		return redirect(url_for('.loadHomeScreen'))
	except Exception as e:
            # Exception handler pinpointing location of error raised
            # Extract source: https://www.codegrepper.com/code-examples/python/python+get+line+number+of+error
            # Website url: https://www.codegrepper.com/
            # Author: Confused Cottonmouth
            # Access date: 11/2021
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

@app.route('/search', methods=['POST','GET'])
def searchItems():
    try:
        #Search function request method issued
        if request.method == 'POST':
            
            databaseStringSearch = []
            for counter in request.form:
                databaseStringSearch.append(counter)
            
            databaseStringSearch.pop(len(databaseStringSearch) - 1)
            con = sqlite3.connect('./Database/bookProducts.db')
            cur = con.cursor();
            
            row = []
            
            counter = 0
            for selection in databaseStringSearch:
                cur.execute("SELECT * FROM products WHERE author_name = ?", [selection])
                row.append(cur.fetchone())
            
            
            
        else:
            return redirect(url_for('.loadBookProducts')) 

        
    except Exception as e:
        # Exception handler pinpointing location of error raised
        # Extract source: https://www.codegrepper.com/code-examples/python/python+get+line+number+of+error
        # Website url: https://www.codegrepper.com/
        # Author: Confused Cottonmouth
        # Access date: 11/2021
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    finally:
        return redirect(url_for('.loadBookProducts'))

def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False	


