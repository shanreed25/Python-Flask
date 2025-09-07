from flask import Flask
import random
#Creating app from the Flask class and to initialize a new Flask object
# there is only one require argument, and that is the import name
app = Flask(__name__)#__name__ is a python special attributes
# you can tap into __name__ to find out what the name of the current class, function, method, or descriptor or generator
print(__name__)# prints __main__
# when we get __main__ it means we are executing code in a particular module: https://docs.python.org/3/library/__main__.html
#  __main__ is the name of the scope in which top-level code executes
# A module’s __name__ is set equal to '__main__' when read from standard input, a script,
# or from an interactive prompt but not from an imported module https://docs.python.org/3.9/library/__main__.html

print(random.__name__)# prints random because it is read from a module

# .route() is a python decorator function that lives inside the app object(declared in the Flask class)
@app.route("/")# this function only triggers if the user is accessing the('/') route
def hello_world():
    return "<p>Hello, World!</p>"#converts this into a HTML page

@app.route("/bye")# this function only triggers if the user is accessing the('/bye') route
def say_bye():
    return "Bye"


# To run the application, use the `flask` command or `python -m flask`.
# You need to tell the Flask where your application is with the --app option
# In the terminal/command line/shell run:  `flask --app hello run`

#*************************************************************************************

# common ways people run Flask apps
if __name__ == "__main__":# if true we are running this code from within the current file
    # execute only if run as a script
    app.run()#does the same thing as executing `flask --app hello run` in the terminal
    # then we can use the run and stop buttons instead of running `flask --app hello run` and using `CTRL+C` in the terminal



