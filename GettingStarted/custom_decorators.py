from flask import Flask
from functools import wraps


app = Flask(__name__)

def make_h1(f):# decorator function: takes a function `f` (which will be your Flask view function) as an argument

    # for preserving the metadata, like its name and docstrings, of the original function f
    # is important for Flask's internal workings, especially when dealing with multiple decorators or url_for
    @wraps(f)

    def h1_function(*args, **kwargs):
        content = f(*args, **kwargs)# calls the original view function f and captures its return value (the content you want to display).
        return f"<h1>{content}</h1>"# then wraps this content within an <h1> tag using an f-string and returns the modified HTML string
    return h1_function

#OR*****************************************************************************
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
# you apply your custom decorator below the @app.route decorator
# the order of decorators matters in Flask; @app.route should generally be the outermost decorator.
@make_h1
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"  # h1 tag bold, italic and underlined

# @app.route("/")
# def hello_world():
#     return "<h1><b><em><u>Hello, World!</em></u><b></h1>"# h1 tag bold, italic and underlined

if __name__ == '__main__':
    app.run(debug=True)
