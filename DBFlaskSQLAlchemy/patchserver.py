from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB: your application's database models (e.g., User, Product, Order) will then inherit from this Base class.
# This centralizes the ORM setup and makes it easy to manage your models
class Base(DeclarativeBase):# DeclarativeBase serves as the base class for all your ORM-mapped models
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db' # Configure the Database URI

# creates an instance of the SQLAlchemy class, which is the core of the Flask-SQLAlchemy extension.
# this db object will then be used to interact with your database within your Flask application
db = SQLAlchemy(model_class=Base)# model_class=Base argument tells Flask-SQLAlchemy to use a custom base class for your database models instead of its default db.Model

# connects the SQLAlchemy database instance (db) to a specific Flask application instance (app),
# enabling the extension to function correctly within that application's context.
db.init_app(app)


# Cafe TABLE Configuration: Define Database Models
class Cafe(db.Model):# inherit from db.Model, provided by Flask-SQLAlchemy
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

# for converting it to a dictionary to use return jsonify(cafe=random_cafe.to_dict()) in the get_cafe function
    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# this construct creates a temporary application context. When you wrap db.create_all() within with app.app_context():,
# you are explicitly telling Flask to push an application context for the duration of that block. This ensures that
# db.create_all() has the necessary context to locate the app instance and its configurations, allowing it to connect
# to the database and create the tables based on your defined models
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP PUT/PATCH - Update Record
# if a user wanted to submit a change on particular field
# the id of the café, which you can get by making a GET request to fetch data on all the cafes,
# then you can update the field you want of the café
# PATCH request is more efficient, as we don't need to change any of the rest of the cafe's data
# Updating the price of a cafe based on a particular id:
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(entity=Cafe, ident=cafe_id)  # Returns None if cafe_id is not found
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# Updating the price of a cafe based on a particular id:
# http://127.0.0.1:5000/update-price/CAFE_ID?new_price=£5.67
# Notice that even when the resource is not found and we get an error the correct HTTP code is not being returned.
# It should be 404 for "resource not found" but instead we're getting 200 for "a ok".
# @app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
# def patch_new_price(cafe_id):
#     new_price = request.args.get("new_price")
#     try:
#         cafe = db.get(Cafe, cafe_id)
#     except AttributeError:
#         return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
#     else:
#         cafe.coffee_price = new_price
#         db.session.commit()
#         return jsonify(response={"success": "Successfully updated the price."}), 200



if __name__ == '__main__':
    app.run(debug=True)
