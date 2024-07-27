#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. /hbnb: display “HBNB”
3. /c/<text>: display “C ” followed by
the value of the text variable
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
