from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, Length
import email_validator # additional package to get email validation to work
from flask_bootstrap import Bootstrap4


# Define your form fields and validators in a Python class that inherits from FlaskForm
class LoginForm(FlaskForm):
    # validators parameter accepts a List of validator Objects
    # DataRequired makes the fields required fields, so the user must type something, otherwise an error will be generated
    #  if you leave a field empty, it might give you a pop-up,
    #  this behaviour is not from our validator, in fact it's a built-in mechanism that varies from browser to browser
    # to make sure that we are giving all users field validation, we have to switch off the browser validation,
    # and we do that with an attribute on the form element called novalidate
    # email = StringField('Email', validators=[DataRequired()])
    # password = StringField('Password', validators=[DataRequired()])

# this code can be  improved
#     email = StringField('Email')
#     password = StringField('Password')
#     submit = SubmitField('Submit')

# arguments given when creating a StringField or PasswordField is for the label property of the form field
    # it is a good idea to add the keyword argument when it's not clear what the argument is for
    email = StringField(label='Email',  validators=[
        DataRequired(message="Email is required."),
        #Validates an email address. Requires email_validator package to be installed
        Email(message="Please enter a valid email address (e.g., user@example.com).")])
    password = PasswordField(label='Password', validators=[
        DataRequired(message="Password is required."),
        Length(min=8, message="Password must be at least 8 characters long.")# Validates the length of a string

    ]) # PasswordField()will obscure the text typed into the input
    submit = SubmitField(label='Log In')

app = Flask(__name__)

# a secret key in your main.py, which will be used to generate the csrf_token
app.secret_key = "some secret string"
# "/" is a static path, but its always a good idea to use dynamically built urls like this "/login"
@app.route("/")
def home():
    return render_template('index.html')


# tell our form to validate the user's entry when they hit submit
# the route must be able to respond to POST requests and then to validate_on_submit()
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()# to validate_on_submit()

    # # check the return value of validate_on_submit() which will be True if validation was successful
    # # after the user submitted the form, or False if it failed
    # if login_form.validate_on_submit():
    #     # to get hold of the form data you tap into the
    #     # <form_object>.<form_field>.data
    #     email = login_form.email.data
    #     print(email)

    #  if the form was submitted and validated and their credentials matched
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
