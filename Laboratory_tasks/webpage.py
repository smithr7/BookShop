from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"<p>Hello, 5001CEM!<br>You went to {url_for('hello_world')} to get here</p>"

@app.route('/name/<myname>')

def hello_person(myname):
    return f"<p>Hello, {escape(myname)}!<br>You went to {url_for('hello_person',myname=escape(myname))}</p>"

@app.route('/age/<int:age>')

def hello_age(age):
    return f'<p>Hello,person who is {escape(age)} years old!</p>'

@app.route('/pleased/<name>')
def pleased(name):
    return render_template('hello.html',myname=name,n=10)