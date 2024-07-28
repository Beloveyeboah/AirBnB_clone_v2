#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. /hbnb: display “HBNB”
3. /c/<text>: display “C ” followed by
the value of the text variable
4. python/<text>: display “Python ”,
followed by the value of the text
5. display “n is a number” only if n is an integer
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ this route dispalays hbnb
    """

    msg = 'HBNB'

    return msg


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    display “C ” followed by the value of the text
    """

    new_string = text.replace('_', ' ')
    return 'C {}'.format(new_string)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text='is cool'):
    """
    display “python ” followed by the value of the text
    """

    if text:
        msg = text.replace('_', ' ')
    return 'Python {}'.format(msg)


@app.route('/number/<int:n>',  strict_slashes=False)
def is_number(n):
    """ display “n is a number” only if n is an integer
    """

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number(n=None):
    """display a HTML page only if n is an integer"""

    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n=None):
    if isinstance(n, int):
        if n % 2 == 0:
            msg = 'even'
        else:
            msg = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, msg=msg)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
