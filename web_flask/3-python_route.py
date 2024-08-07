#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. /hbnb: display “HBNB”
3. /c/<text>: display “C ” followed by
the value of the text variable
4. python/<text>: display “Python ”,
followed by the value of the text
"""

from flask import Flask

app = Flask("__name__")


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
