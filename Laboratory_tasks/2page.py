from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "<p>Hello, 5001CEM!</p>"

@app.route('/name/<myname>')

def hello_person(myname):
        return f'<p>Hello, {escape(myname)}!</p>'

@app.route('/age/<int:age>')

def hello_age(age):
    return f'<p>Hello,person who is {escape(age)}years old!</p>'

