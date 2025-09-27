from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, Length
import email_validator # additional package to get email validation to work
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField(label='Email',  validators=[
        DataRequired(message="Email is required."),
        Email(message="Please enter a valid email address (e.g., user@example.com).")])
    password = PasswordField(label='Password', validators=[
        DataRequired(message="Password is required."),
        Length(min=8, message="Password must be at least 8 characters long.")
    ])
    submit = SubmitField(label='Log In')

app = Flask(__name__)

app.secret_key = "some secret string"
bootstrap = Bootstrap5(app) # initialise bootstrap-flask


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)
if __name__ == '__main__':
    app.run(debug=True)
