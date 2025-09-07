from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/<name>")#creating a variable within a url by using this syntax <variable_name>, default type is a string
#when the decorator is done with the variable, the function receives the variable name and it can be used inside the function
def hello(name):
    return f"Hello {name}, how are you"

@app.route("/username/<user>")#can add something before the variable
def greet(user):
    return f"Hello user {user}"

@app.route("/username/<user>/12")#can add something after the variable
def time_greet(user):
    return f"Hello user {user} it is 12"

@app.route("/user/<path:user>")#given http://127.0.0.1:5000/user/Shannon/Lewis
def name_greet(user):
    return f"Hello user {user}"# returns Hello user Shannon/Lewis

@app.route("/userage/<user>/<int:age>")#mutiple variables
def age_greet(user, age):
    return f"Hello user {user}, you are {age} years old"# returns Hello user Shannon, you are 36

if __name__ == "__main__":
# debug=True
    # By enabling debug mode, the server will automatically reload if code changes,
    # and will show an interactive debugger in the browser if an error occurs during a request
    # The debugger allows executing arbitrary Python code from the browser.
    # It is protected by a pin, that is give to you in the console
        # if you open the Interactive debugger in the browser you will need this pin to access it
        # anyone cannot go and mess with the code without the pin
    # but still represents a major security risk. Do not run the development server or debugger in a production environment
    app.run(debug=True)


