#!/usr/bin/python3
""" creating an html with flask
1. the server listens on 0.0.0.0 on port 5000
2. routs / - display 'Hello HBNB!
3. route /hbnb - dispay 'hbnb '
4. create a /c/<text> route - display the text on the page
5. create a /python/<text> route - default text is "is cool"
6. create a /number/<n> route
"""

from flask import Flask
from flask import render_template

app = Flask("__name__")

# task 0


@app.route("/", strict_slashes=False)
def display():
    """ the root of the wed page"""

    return 'Hello HBNB!'

# task 1


@app.route("/hbnb", strict_slashes=False)
def hbnd():
    """the /hbnb page of the server"""

    return 'HBNB'

# task 2


@app.route("/c/<text>",  strict_slashes=False)
def c_text(text):
    """ (replace underscore _ symbols with a space)"""

    formated_text = text.replace('_', ' ')
    return "C {}".format(formated_text)


# task 3


@app.route("/python/", defaults={"text": 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """

    display_text = text.replace('_', ' ')
    return "Python {}".format(display_text)


# task 4


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """ display “n is a number” only if n is an integer
    """

    return "{} is a number".format(n)

# task 5


@app.route('/number_template/<int:n>', strict_slashes=False)
def dispay_int_html(n):
    """ display a HTML page only if n is an integer"""

    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)