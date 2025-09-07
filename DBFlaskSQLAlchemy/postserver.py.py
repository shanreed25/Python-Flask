from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


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


#  test your API in Postman without building out a WTForm or HTML Form


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)