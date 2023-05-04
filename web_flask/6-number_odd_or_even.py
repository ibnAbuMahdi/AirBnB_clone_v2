#!/usr/bin/python3
""" hello and hbnb route module """
from flask import Flask
from os import environ
from flask import render_template
app = Flask(__name__)
environ.FLASK_APP = '6-numer_odd_or_even.py'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_():
    """ Displays hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """ Display C <text>"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def hello_python(text='is cool', strict_slashes=False):
    """ Displays Python <text='is cool'>"""
    return 'Python {}'.format(text.replace('_', " "))


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ Display <n> is number if n is number """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Displays template with number """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """ Displays template with odd or even number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')